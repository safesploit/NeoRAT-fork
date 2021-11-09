from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.utility.delete_client import *


@error_exception_handling
def delete(message):
  index = validate_dict_key(message, 'index')

  if index:
    delete_client(int(index))
  else:
    raise Exception('Error message')