import csv

from domestic.utility.status_message import *
from domestic.make.make_directories import *
from domestic.utility.get_filename import *
from domestic.global_state import *


def make_history(directories, file_type, browserhistory, success_message=None):
  filename = get_filename(file_type)
  username = state['session']['username']
  path = f'{state["root"]}/{username}/{directories[-1]}'
  directories_to_make = [username] + [f'{username}/{directory}' for directory in directories]
  make_directories(directories_to_make)

  for browser, history in browserhistory.items():
    with open(f'{path}/{browser}_{filename}', 'w', encoding='utf-8', newline='') as csvfile:
      csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)        

      for data in history:
        csv_writer.writerow(data)

  if success_message:
    status_message(f'Path: {path}/[browser]_{filename}\n{success_message}', 'success')