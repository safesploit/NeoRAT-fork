from binary.data_handling.send_data import *
from foreign.global_state import *


def error_exception_handling(func):
  def func_wrapper(conn, data):
    try:
      func(conn, data)
    except Exception as err:
      send_data(conn, {'message': f'Error: {err}\nPlease validate your input & try again', 'text_mode': 'danger'}, (state['settings']['encryption'], state['settings']['encoding'], state['settings']['headersize']))
  return func_wrapper