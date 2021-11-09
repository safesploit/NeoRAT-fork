import threading
import ctypes

from foreign.parse.crash_exception_handling import *


@crash_exception_handling
def messagebox_action(title, text, style):
  ctypes.windll.user32.MessageBoxW(0, text, title, style)


def messagebox(title, text, style):
  threading.Thread(target=messagebox_action, args=(title, text, style), daemon=True).start()
  return {'message': f'Messagebox succesfully shown', 'text_mode': 'success'}