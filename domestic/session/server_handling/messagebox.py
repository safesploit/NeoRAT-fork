from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *


@error_exception_handling
def messagebox(message):
  title = validate_dict_key(message, 'title', False)
  text = validate_dict_key(message, 'text', False)
  style = validate_dict_key(message, 'style')

  if title and text:
    if style == 'info':
      message['style'] = 64
    elif style == 'cross':
      message['style'] =  16
    elif style == 'question':
      message['style'] =  32
    elif style == 'warning':
      message['style'] =  48
    else:
      message['style'] = 64
    session_message(message)
  else:
    raise Exception('Error message')