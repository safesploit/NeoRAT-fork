from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.global_state import *


@error_exception_handling
def enter_session(message):
  index = validate_dict_key(message, 'index')

  if index:
    state['session'] = {'active': True, 'socket': state['sockets']['clients'][0][int(index)], 'username': state['sockets']['clients'][2][int(index)]['username'], 'data': None}
    status_message('Session succesfully established', 'success')
  else:
    raise Exception('Error message')