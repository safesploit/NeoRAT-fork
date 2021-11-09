import win32gui
import win32con

from foreign.utility.terminal_pipe import *


def system(action_type, extra_data):
  if action_type == 'shutdown':
    return {'message': terminal_pipe('shutdown /p /f', extra_data[0], extra_data[1])}
  elif action_type == 'restart':
    return {'message': terminal_pipe('shutdown /r /f /t 0', extra_data[0], extra_data[1])}    
  elif action_type == 'logout':
    return {'message': terminal_pipe('shutdown /l /f', extra_data[0], extra_data[1])}    
  elif action_type == 'standby':
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
    return {'message': 'Successfully activated standby mode', 'text_mode': 'success'}
  else:
    raise Exception('Error message')