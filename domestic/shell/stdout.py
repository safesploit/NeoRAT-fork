from domestic.utility.status_message import *


def stdout(low_message, message):
  if low_message == '':
    status_message(None, 'program')
  else:
    status_message(f'\'{message["message"]}\' command could not be found\nUse \'help\' command for assistance', 'warning')