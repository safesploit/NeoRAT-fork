from colorama import init, Fore, Style
init()

from domestic.utility.validate_dict_key import *
from domestic.global_state import *


def status_message(data, status, options={}):
  dots = validate_dict_key(options, 'dots')
  exclamation_point = validate_dict_key(options, 'point')
  end = validate_dict_key(options, 'end')
  custom = validate_dict_key(options, 'custom')
  session = state['session']['active']
  username = state['session']['username']
  name = state['name']
  end_result = ''

  if status == 'raw':
    print(f'{Fore.CYAN}{data}{Style.RESET_ALL}')
    return    

  try:
    messages = [x for x in data.split('\n') if x != '']
  except:
    messages = [None]

  if exclamation_point == 'empty':
    exclamation_point = ''
  elif exclamation_point == 'dot':
    exclamation_point = '.'
  elif exclamation_point:
    exclamation_point = '!'
  elif status == 'success':
    exclamation_point = '!'
  else:
    exclamation_point = '.'

  if dots:
    dots = '..'
  else:
    dots = ''

  if end:
    end_result = ''
  else:
    end_result = f'\n{Fore.BLUE}{name}{Style.RESET_ALL}{Fore.RED}>{Style.RESET_ALL}'

  if custom:
    custom = f'\b{custom}'
  else:
    custom = ''

  if session:
    if end:
      end_result = ''
    else:
      end_result = f'\n{Fore.BLUE}{username}{Style.RESET_ALL} {Fore.RED}=>{Style.RESET_ALL} {Fore.BLUE}Terminal{Style.RESET_ALL}{Fore.RED}>{Style.RESET_ALL}'

  for index, message in enumerate(messages):
    if index == 0 and session and state['settings']['loading']:
      print(' ' * 25, end='\r')

    if status == 'success':
      print(f'{Fore.GREEN}[{Style.RESET_ALL}+{custom}{Fore.GREEN}]{Style.RESET_ALL} {Fore.GREEN}{message}{exclamation_point}{dots}{Style.RESET_ALL}')
    elif status == 'danger':
      print(f'{Fore.RED}[{Style.RESET_ALL}-{custom}{Fore.RED}]{Style.RESET_ALL} {Fore.RED}{message}{exclamation_point}{dots}{Style.RESET_ALL}')
    elif status == 'warning':
      print(f'{Fore.YELLOW}[{Style.RESET_ALL}!{custom}{Fore.YELLOW}]{Style.RESET_ALL} {Fore.YELLOW}{message}{exclamation_point}{dots}{Style.RESET_ALL}')
    elif status == 'primary':
      print(f'{Fore.BLUE}[{Style.RESET_ALL}i{custom}{Fore.BLUE}]{Style.RESET_ALL} {Fore.BLUE}{message}{exclamation_point}{dots}{Style.RESET_ALL}')
    elif status == 'magenta':
      print(f'{Fore.MAGENTA}[{Style.RESET_ALL}i{custom}{Fore.MAGENTA}]{Style.RESET_ALL} {Fore.MAGENTA}{message}{exclamation_point}{dots}{Style.RESET_ALL}')
    elif status == 'pure':
      print(f'{Fore.CYAN}{message}{Style.RESET_ALL}')
    elif status == 'loading':
      print(f'{Fore.CYAN}{message}{Style.RESET_ALL}', end='\r', flush=True)
    elif status == 'program':
      if session:
        print(f'{Fore.BLUE}{username}{Style.RESET_ALL} {Fore.RED}=>{Style.RESET_ALL} {Fore.BLUE}Terminal{Style.RESET_ALL}{Fore.RED}>{Style.RESET_ALL}', end='')
      else:
        print(f'{Fore.BLUE}{name}{Style.RESET_ALL}{Fore.RED}>{Style.RESET_ALL}', end='')
    else:
      raise Exception('Invalid color selection')
    
    if index == (len(messages) -1) and status != 'program':
      print(end=end_result)