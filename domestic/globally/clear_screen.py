import os

from domestic.utility.status_message import *


def clear_screen():
  os.system('cls')
  status_message(None, 'program')