from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *


@error_exception_handling
def image(message):
  monitor = validate_dict_key(message, 'monitor')
  screenshot = validate_dict_key(message, 'screenshot')
  cam = validate_dict_key(message, 'cam')
  
  assert screenshot or cam

  if monitor is None:
    message['monitor'] = 0
  else:
    message['monitor'] = int(monitor)

  if screenshot:
    message['image_type'] = True
    del message['screenshot']
    image_type = 'screenshot'
  else:
    message['image_type'] = False
    del message['cam']
    image_type = 'cam-screenshot'

  data = session_message(message, False)

  if data['screenshot']:
    make_image(['image', f'image/{image_type}'], data['screenshot'], success_message=data['message'], image_type=message['image_type'])