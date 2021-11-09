import sys
import os

from foreign.global_state import *


def uninstall():
  os.remove(state['file'])
  sys.exit(0)