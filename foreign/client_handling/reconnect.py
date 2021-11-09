import threading

from foreign.utility.terminal_pipe import *
from foreign.global_state import *


def reconnect(extra_data):
  threading.Thread(target=terminal_pipe, args=(f'{state["file"]} -ip {state["ip"]} -p {state["port"]}', extra_data[0], extra_data[1])).start()
  return {'message': 'Reconnecting client', 'text_mode': 'success'}