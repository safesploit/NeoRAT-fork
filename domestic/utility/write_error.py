from domestic.global_state import *


def write_error(error):
  if state['settings']['debug']:
    print(f'Error: {error}')