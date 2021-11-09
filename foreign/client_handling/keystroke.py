import threading
import time

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from foreign.parse.crash_exception_handling import *


@crash_exception_handling
def keystroke_action(inject):
  keyboard = KeyboardController()
  mouse = MouseController()

  for command in inject:
    command = command.split(' ')
    c_type, c_data = command[0], command[1]

    if c_type == 'press': 
      try:
        c_data = eval(f'Key.{c_data}')
      except:
        pass
      finally:
        keyboard.press(c_data)
        keyboard.release(c_data)
    elif c_type == 'hold':
      try:
        c_data = eval(f'Key.{c_data}')
      except:
        pass
      finally:
        keyboard.press(c_data)
    elif c_type == 'release':
      try:
        c_data = eval(f'Key.{c_data}')
      except:
        pass
      finally:
        keyboard.release(c_data)
    elif c_type == 'type':
      keyboard.type(' '.join(command[1:]))
    elif c_type == 'position':
      mouse.position = [int(position) for position in c_data.split(',')]
    elif c_type == 'move':
      move_positions = [int(position) for position in c_data.split(',')]
      mouse.move(move_positions[0], move_positions[1])
    elif c_type == 'mhold':
      mouse.press(eval(f'Button.{c_data}'))
    elif c_type == 'mrelease':
      mouse.release(eval(f'Button.{c_data}'))
    elif c_type == 'click':
      mouse.press(eval(f'Button.{c_data}'))
      mouse.release(eval(f'Button.{c_data}'))
    elif c_type == 'dclick':
      mouse.click(eval(f'Button.{c_data}'), 2)
    elif c_type == 'scroll':
      scroll_positions = [int(position) for position in c_data.split(',')]
      mouse.scroll(scroll_positions[0], scroll_positions[1])
    elif c_type == 'sleep':
      time.sleep(float(c_data))
    else:
      raise Exception('Invalid keystroke command')


def keystroke(inject):
  threading.Thread(target=keystroke_action, args=(inject,), daemon=True).start()
  return {'message': 'Keystroke thread started', 'text_mode': 'primary', 'text_extras': {'point': True}}