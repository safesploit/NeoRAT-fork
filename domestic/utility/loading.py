import threading
import time
import sys

from domestic.utility.status_message import *
from domestic.global_state import *


def loading(text, blacklist):
  if state['settings']['loading-animation']:
    start_time = time.time()
    
    while True:
      for i in range(len(text)):
        if not state['settings']['dynamic']['is-loading']:
          sys.exit(0)
        if text[i].lower() in blacklist:
          continue
        text = text[:i].lower() + text[i:].capitalize()
        time_taken = time.time() - start_time
        status_message(f'[{time_taken:.1f}] {text}', 'loading', {'end': True})
        time.sleep(0.1)
  else:
    status_message(text.capitalize(), 'loading', {'end': True})

def start_loading(text, blacklist=('.', ' ')):
  state['settings']['dynamic']['is-loading'] = True
  threading.Thread(target=loading, args=(text, blacklist), daemon=True).start()

def stop_loading():
  state['settings']['dynamic']['is-loading'] = False