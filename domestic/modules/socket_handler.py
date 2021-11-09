import socket

from domestic.utility.status_message import *
from domestic.utility.write_error import *
from domestic.global_state import *


def bind_socket(ip, port, module_type, stdout=True):
  try:
    state['sockets']['modules'][module_type][0] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    state['sockets']['modules'][module_type][0].bind((ip, int(port)))
    state['sockets']['modules'][module_type][0].listen()
  except Exception as err:
    write_error(err)
    state['sockets']['modules'][module_type][0] = None
    raise Exception('Socket binding error')
  else:
    if stdout:
      status_message(f'{module_type.capitalize()} address successfully bound', 'success')

def close_client(index, module_type, write_stdout=True):
  state['sockets']['modules'][module_type][1][int(index)][0].close()

  if write_stdout:
    status_message(f'{module_type.capitalize()} client successfully closed', 'success')

def unbind_socket(module_type):
  for _ in range(len(state['sockets']['modules'][module_type][1])):
    close_client('0', module_type, False)

  state['sockets']['modules'][module_type][0].close()
  state['sockets']['modules'][module_type][0] = None
  status_message(f'{module_type.capitalize()} address successfully closed', 'success')