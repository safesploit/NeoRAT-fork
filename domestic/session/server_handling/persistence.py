from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *


@error_exception_handling
def persistence(message):
  elevate = validate_dict_key(message, 'elevate')
  service = validate_dict_key(message, 'service')
  schedule = validate_dict_key(message, 'schedule')
    
  if elevate:
    message['action_type'] = 'elevate'
    del message['elevate']
  elif service:
    message['action_type'] = 'service'
    del message['service']
  elif schedule:
    message['action_type'] = 'schedule'
    del message['schedule']
  else:
    raise Exception('Error message')

  session_message(message)