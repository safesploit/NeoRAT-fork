from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.global_state import *


@error_exception_handling
def system(message):
  shutdown = validate_dict_key(message, 'shutdown')
  restart = validate_dict_key(message, 'restart')
  logout = validate_dict_key(message, 'logout')
  standby = validate_dict_key(message, 'standby')

  if shutdown:
    message['action_type'] = 'shutdown'
    del message['shutdown']
  elif restart:
    message['action_type'] = 'restart'
    del message['restart']
  elif logout:
    message['action_type'] = 'logout'
    del message['logout']
  elif standby:
    message['action_type'] = 'standby'
    del message['standby']
  else:
    raise Exception('Error message')
  
  session_message(message)