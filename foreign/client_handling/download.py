import os


def download(filename, max_file_size):
  if (os.path.getsize(filename) / 1024 / 1024) > max_file_size:
    return {'message': f'File exceeding maximum size of {max_file_size}MB', 'download': None, 'text_mode': 'danger'}

  with open(filename, 'rb') as f:
    return {'message': f'{filename} succesfully downloaded', 'download': f.read(), 'text_mode': 'success'}