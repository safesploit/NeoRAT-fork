import multiprocessing

from subprocess import Popen, PIPE

from foreign.global_state import *


def get_terminal_pipe_data(data, return_dict):
  encoding = state['settings']['encoding']
  shell = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
  stdout, stderr = shell.communicate()
  return_dict['result'] = '{}{}'.format(stdout.decode(encoding), stderr.decode(encoding)).strip('\r\n').replace('ÿ', ' ')

  if return_dict['result'] == '':
    return_dict['result'] = 'Empty Response'
  
  return return_dict['result']
  

def terminal_pipe(data, safe, timeout):
  if safe:
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    terminal_data = multiprocessing.Process(target=get_terminal_pipe_data, args=(data, return_dict), daemon=True)
    terminal_data.start()
    terminal_data.join(timeout)

    if terminal_data.is_alive():
      return_dict['result'] = f'Timeout reached of {timeout} seconds'
      terminal_data.terminate()
      terminal_data.join()

    return return_dict['result']
  else:
    return get_terminal_pipe_data(data, {})