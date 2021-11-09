import os

from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.make.make_directories import *
from domestic.global_state import *


@error_exception_handling
def download(message):
  assert message['file']

  filename = validate_dict_key(message, 'file')
  execute = validate_dict_key(message, 'execute')

  username = state['session']['username']
  make_directories([username, f'{username}/downloads'])
  root = f'{state["root"]}/{username}/downloads/{filename}'

  message['max_file_size'] = state['settings']['max-file-size']
  if execute:
    del message['execute']

  data = session_message(message, False, loading_text='downloading file...')
  download = validate_dict_key(data, 'download', False)
  
  if download:
    with open(root, 'wb') as f:
      f.write(download)
    
    if execute:
      os.startfile(root)

  status_message(data['message'], data['text_mode'])