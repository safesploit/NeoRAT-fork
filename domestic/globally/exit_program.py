import os

from domestic.utility.status_message import *
from domestic.utility.delete_client import *
from domestic.global_state import *


def exit_program():
  status_message(f'Exiting {state["name"]}', 'danger', {'dots': True, 'end': True})

  for i in range(len(state['sockets']['clients'][0])):
    delete_client(i, False)

  os._exit(0)