from domestic.parse.error_exception_handling import *
from domestic.session.session_message import *


@error_exception_handling
def cd(message):
  assert message['to']
  session_message(message)