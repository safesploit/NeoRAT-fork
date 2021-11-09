from domestic.utility.validate_dict_key import *
from domestic.utility.status_message import *
from domestic.utility.write_error import *
from domestic.globally.get_help import *
from domestic.global_state import *


def error_exception_handling(func):
	def func_wrapper(*args):
		try:
			number_of_arguments = len(args)

			if number_of_arguments == 1:
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

			if state['session']['active'] and func.__name__ in [*state['sockets']['modules']]:
				func_key = validate_dict_key(help_obj, f'{func.__name__}_2', False)
			elif func.__name__ == 'listening':
				func_key = validate_dict_key(help_obj, 'listen', False)
			else:
				func_key = validate_dict_key(help_obj, func.__name__, False)

			if func_key:
				status_message(f'An exception was reached, please verify your input & try again\nUsage: {func_key["usage"]}', 'danger')
			else:
				status_message('Exception was reached, something went wrong\nPlease validate your input & try again', 'danger')
	return func_wrapper