import pyaudio
import cv2

from desktopmagic.screengrab_win32 import getDisplayRects


def device_support(silent, io_channels):
  device_obj = {}

  try:
    device_obj['monitors'] = len(getDisplayRects())
  except:
    device_obj['monitors'] = '???'

  if silent:
    device_obj['cams'] = '???'
  else:
    cams = [0, []]

    while True:
      cam = cv2.VideoCapture(cams[0])
      check, frame = cam.read()
      if not check:
        break
      cams[0] += 1
      cams[1].append(f'[{int(cam.get(3))},{int(cam.get(4))}]')
    
    cam.release()
    device_obj['cams'] = '{} {}'.format(cams[0], ', '.join(cams[1]))

  try:
    p = pyaudio.PyAudio()
    CHUNK = 81920
    FORMAT = pyaudio.paInt16
    RATE = 44100
  except:
    device_obj['io-channels'] = '???'
  else:
    try:
      try:
        stream = p.open(format=FORMAT, channels=2, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        input_channels = '2'
      except:
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        input_channels = '1'

      if io_channels[0] in ('1', '2'):
        device_obj['io-channels'] = '{}(+), '.format(input_channels)
      else:
        device_obj['io-channels'] = '{}(-), '.format(input_channels)
    except:
      device_obj['io-channels'] = 'None, '
    
    try:
      try:  
        stream = p.open(format=FORMAT, channels=2, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        output_channels = '2'
      except:
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        output_channels = '1'
      
      if io_channels[1] in ('1', '2'):
        device_obj['io-channels'] += '{}(+)'.format(output_channels)
      else:
        device_obj['io-channels'] += '{}(-)'.format(output_channels)
    except:
      device_obj['io-channels'] += 'None'

    p.terminate()

  return device_obj