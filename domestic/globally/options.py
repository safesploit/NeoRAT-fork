from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.utility.status_message import *
from domestic.global_state import *


options_list = (
  (
  'mode/safe',
  'mode/silent',
  'validation/duplicates',
  'validation/max-clients',
  'information-gathering/history',
  'information-gathering/whoami',
  'information-gathering/record/stream',
  'information-gathering/record/cam-stream',
  'information-gathering/record/audio',
  'information-gathering/record/talk',
  'information-gathering/save/screenshot',
  'information-gathering/save/cam-screenshot',
  'information-gathering/backup/text',
  'information-gathering/backup/image',
  'notice/email-notice',
  'notice/email-data/email',
  'notice/email-data/password',
  'notice/email-data/to'
  ),
  (
    'bool',
    'bool',
    'bool',
    'int',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'bool',
    'str',
    'str',
    'str'
  )
)


@error_exception_handling
def options(message):
  key = validate_dict_key(message, 'key')
  value = validate_dict_key(message, 'value')
  available = validate_dict_key(message, 'available')

  if key and value:
    key_list = key.split('/')
    key_len = len(key_list)

    assert key in options_list[0]
    value = validate_option(value, options_list[1][options_list[0].index(key)])

    if key_len == 2:
      state['options'][key_list[0]][key_list[1]] = value
    elif key_len == 3:
      state['options'][key_list[0]][key_list[1]][key_list[2]] = value
    elif key_len == 4:
      state['options'][key_list[0]][key_list[1]][key_list[2]][key_list[3]] = value
    else:
      raise Exception('Key length is invalid')
    status_message(f'Option: {key} is now set to {value}', 'success')
  elif available:
    options = state['options']
    categories = ['mode', 'validation', 'information-gathering', 'notice']

    for categorie in categories:
      option_category = options[categorie]

      status_message(f'{categorie.capitalize()}:', 'magenta', {'end': True, 'point': 'empty'})
      for key, value in option_category.items():
        if 'dict' in str(type(value)):
          status_message(f'- {key.capitalize()}:', 'magenta', {'end': True, 'point': 'empty'})
          for key_2, value_2 in value.items():
            status_message(f'        - {key_2.capitalize()}: {value_2}', 'pure', {'end': True})
        else:
          status_message(f'    - {key.capitalize()}: {value}', 'pure', {'end': True})
      print()
    status_message(None, 'program')
  else:
    raise Exception('Error message')


def validate_option(value, value_type):
  if value == 'true':
    value = True
  elif value == 'false':
    value = False
  elif value == 'none':
    if 'str' == value_type:
      value = None
  elif value.isdigit():
    value = int(value)

  value_type_calc = str(type(value))

  if 'str' in value_type_calc:
    assert len(value) < 128
  elif 'int' in value_type_calc:
    assert value < 10000

  assert value_type in value_type_calc or value is None

  return value