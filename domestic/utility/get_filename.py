import time


def get_filename(file_type):
  return time.strftime(f'%Y-%m-%d (%H-%M-%S).{file_type}')