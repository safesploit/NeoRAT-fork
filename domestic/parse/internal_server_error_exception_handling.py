import sys

from domestic.utility.write_error import *


def internal_server_error_exception_handling(func):
  def func_wrapper(*args):
    try:
      number_of_arguments = len(args)
      
      if number_of_arguments == 0:
        func()
      elif number_of_arguments == 1:
        func(args[0])
      elif number_of_arguments == 2:
        func(args[0], args[1])
      elif number_of_arguments == 3:
        func(args[0], args[1], args[2])
      elif number_of_arguments == 4:
        func(args[0], args[1], args[2], args[3])
      elif number_of_arguments == 5:
        func(args[0], args[1], args[2], args[3], args[4])
      elif number_of_arguments == 6:
        func(args[0], args[1], args[2], args[3], args[4], args[5])
      elif number_of_arguments == 7:
        func(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
    except Exception as err:
      write_error(err)
      sys.exit(0)
  return func_wrapper