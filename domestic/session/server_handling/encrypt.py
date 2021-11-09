from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *


def encrypt(message):
  assert message['file']

  decrypt = validate_dict_key(message, 'decrypt')

  if decrypt is None:
    message['decrypt'] = False

  session_message(message)