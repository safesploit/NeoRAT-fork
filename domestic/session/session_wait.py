import time

from domestic.utility.loading import *
from domestic.global_state import *


def session_wait(queue_obj, loading_text):
  try:
    if state['settings']['loading']:
      start_loading(loading_text)

    state['settings']['dynamic']['queue'].append(queue_obj)

    while state['session']['data'] is None:
      time.sleep(0.1)
    else:
      if state['settings']['loading']:
        stop_loading()
        
      return state['session']['data']
  finally:
    state['session']['data'] = None