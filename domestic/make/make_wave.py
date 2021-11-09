import wave

from domestic.make.make_directories import *
from domestic.utility.get_filename import *
from domestic.global_state import *


def make_wave(directories, username, wave_data):
  filename = get_filename('wav')
  path = f'{state["root"]}/{username}/{directories[-1]}/{filename}'
  directories_to_make = [username] + [f'{username}/{directory}' for directory in directories]
  make_directories(directories_to_make)

  waveFile = wave.open(path, 'wb')
  waveFile.setnchannels(wave_data[0])
  waveFile.setsampwidth(wave_data[1].get_sample_size(wave_data[2]))
  waveFile.setframerate(wave_data[3])
  waveFile.writeframes(b''.join(wave_data[4]))
  waveFile.close()