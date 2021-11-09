from domestic.utility.status_message import *
from domestic.global_state import *


def exit_session(write_stdout=True, data=None):
  state['session'] = {'active': False, 'socket': None, 'username': None, 'data': data}
  
  if write_stdout:
    status_message('Session successfully exited', 'success')