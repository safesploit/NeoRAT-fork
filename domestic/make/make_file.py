from domestic.utility.status_message import *
from domestic.make.make_directories import *
from domestic.utility.get_filename import *
from domestic.global_state import *


def make_file(directories, file_type, data, success_message=None):
  filename = get_filename(file_type)
  username = state['session']['username']
  path = f'{state["root"]}/{username}/{directories[-1]}/{filename}'
  directories_to_make = [username] + [f'{username}/{directory}' for directory in directories]
  make_directories(directories_to_make)

  with open(path, 'wb') as f:
    f.write(data)
  
  if success_message:
    status_message(f'Path: {path}\n{success_message}', 'success')