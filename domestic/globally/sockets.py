from domestic.utility.validate_dict_key import *
from domestic.utility.status_message import *
from domestic.global_state import *


def sockets():
  if state['sockets']['server']:
    ip, port = state['sockets']['server'].getsockname()
    status_message('Server:', 'magenta', {'end': True, 'point': 'empty'})
    status_message(f'    - Listening', 'pure', {'end': True})
  else:
    status_message('Server:', 'magenta', {'end': True, 'point': 'empty'})
    status_message(f'    - Not listening', 'pure', {'end': True})

  for key, value in state['sockets']['modules'].items():
    if value[0]:
      ip, port = value[0].getsockname()
      status_message(f'{key.capitalize()}:', 'magenta', {'end': True, 'point': 'empty'})
    else:
      status_message(f'{key.capitalize()}:', 'magenta', {'end': True, 'point': 'empty'})
      status_message('    - Not listening', 'pure', {'end': True})
      continue

    if len(value[1]) == 0:
      status_message('    - None running', 'pure', {'end': True})
    else:
      for index, module_client in enumerate(value[1]):
        status_message(f'    - [{index}] {module_client[1]}', 'pure', {'end': True})

  print()
  status_message(None, 'program')