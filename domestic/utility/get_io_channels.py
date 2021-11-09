import pyaudio

from domestic.global_state import *


def get_io_channels():
  try:
    p = pyaudio.PyAudio()
    CHUNK = 81920
    FORMAT = pyaudio.paInt16
    RATE = 44100
  except:
    pass
  else:
    try:
      stream = p.open(format=FORMAT, channels=2, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
      stream.stop_stream()
      stream.close()
      state['settings']['io-channels'][0] = '2'
    except:
      try:
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=False, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        state['settings']['io-channels'][0] = '1'
      except:
        pass
      
    try:  
      stream = p.open(format=FORMAT, channels=2, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
      stream.stop_stream()
      stream.close()
      state['settings']['io-channels'][1] = '2'
    except:
      try:
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=False, output=True, frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        state['settings']['io-channels'][1] = '1'
      except:
        pass

    p.terminate()