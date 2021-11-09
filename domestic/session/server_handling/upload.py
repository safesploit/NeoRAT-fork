import os

from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *
from domestic.utility.read_file import *
from domestic.global_state import *


@error_exception_handling
def upload(message):
  filename = validate_dict_key(message, 'file', False)
  url = validate_dict_key(message, 'url', False)
  execute_on_upload = validate_dict_key(message, 'execute')

  message['max_file_size'] = state['settings']['max-file-size']

  if execute_on_upload is None:
    message['execute'] = False
  else:
    message['execute'] = True

  if filename:
    root = f'{state["root"]}/{state["settings"]["folders"]["parent"]}/{state["settings"]["folders"]["child"][0]}/{filename}'

    if (os.path.getsize(root) / 1024 / 1024) > message['max_file_size']:
      status_message(f'File exceeding maximum size of {message["max_file_size"]}MB', 'danger')
      return

    message['from_url'], message['file_data'] = False, read_file(root)
  elif url:
    message['file'], message['from_url'], message['file_data'] = url, True, None
    del message['url']
  else:
    raise Exception('Error message')

  session_message(message, loading_text='uploading file...')