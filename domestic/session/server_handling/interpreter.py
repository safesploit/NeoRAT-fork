from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.utility.read_file import *
from domestic.global_state import *


@error_exception_handling
def interpreter(message):
  execute = validate_dict_key(message, 'execute')
  script = validate_dict_key(message, 'script')
  quiet = validate_dict_key(message, 'quiet')

  assert execute or script

  if script:
    parent_folder = state['settings']['folders']['parent']
    child_folder = state['settings']['folders']['child'][1]
    message['execute'] = read_file(f'{state["root"]}/{parent_folder}/{child_folder}/{script}').decode(state['settings']['encoding'])
    del message['script']

  if quiet:
    del message['quiet']

  data = session_message(message, False)
  result = validate_dict_key(data, 'result')

  if result:
    if quiet is None:
      status_message(data['result'], 'pure', {'end': True})
      print()
    make_file(['interpreter'], 'txt', bytes(data['result'], state['settings']['encoding']), data['message'])
  else:
    status_message(data['message'], data['text_mode'])