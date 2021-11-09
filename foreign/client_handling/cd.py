import os


def cd(directory):
  os.chdir(directory)
  return {'message': f'New directory: {os.getcwd()}', 'text_mode': 'success', 'text_extras': {'point': 'empty'}}