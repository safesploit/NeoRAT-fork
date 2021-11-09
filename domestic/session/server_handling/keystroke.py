from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.read_file import *
from domestic.global_state import *


@error_exception_handling
def keystroke(message):
  inject = validate_dict_key(message, 'inject', False)
  script = validate_dict_key(message, 'script', False)
  
  if inject:
    message['inject'] = inject.strip().split(';')
  elif script:
    parent_folder = state['settings']['folders']['parent']
    child_folder = '{}/{}'.format(state['settings']['folders']['child'][1], state['settings']['folders']['child'][3])
    message['inject'] = read_file(f'{state["root"]}/{parent_folder}/{child_folder}/{script}').decode(state['settings']['encoding']).strip().split('\r\n')
    del message['script']
  else:
    raise Exception('Error message')

  session_message(message)