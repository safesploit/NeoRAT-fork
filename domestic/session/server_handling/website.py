from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *


@error_exception_handling
def website(message):
  message['open'] = message['open'].split(',')
  session_message(message)