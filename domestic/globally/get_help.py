import tabulate

from domestic.utility.status_message import *


help_obj = {
  'help': {
    'type': 'Globally',
    'usage': 'help',
    'description': 'Shows available commands'
  },
  'exit': {
    'type': 'Globally',
    'usage': 'exit',
    'description': 'Exits program'
  },
  'clear': {
    'type': 'Globally',
    'usage': 'clear',
    'description': 'Clears your terminal window'
  },
  'sockets': {
    'type': 'Globally',
    'usage': 'sockets',
    'description': 'Show sockets information'
  },
  'options': {
    'type': 'Globally',
    'usage': 'options --available | --key [key] & --value [value]',
    'description': 'Handle available options'
  },
  'stream': {
    'type': 'Globally',
    'usage': 'stream --ip [ip] & --port [port] | --unbind | --close [index] | --status',
    'description': 'Handle stream module'
  },
  'cam': {
    'type': 'Globally',
    'usage': 'cam --ip [ip] & --port [port] | --unbind | --close [index] | --status',
    'description': 'Handle cam module'
  },
  'audio': {
    'type': 'Globally',
    'usage': 'audio --ip [ip] & --port [port] | --unbind | --close [index] | --status',
    'description': 'Handle audio module'
  },
  'talk': {
    'type': 'Globally',
    'usage': 'talk --ip [ip] & --port [port] | --unbind | --close [index] | --status',
    'description': 'Handle talk module'
  },
  'list': {
    'type': 'Shell',
    'usage': 'list',
    'description': 'List connected clients'
  },
  'server': {
    'type': 'Shell',
    'usage': 'server --ip [ip] & --port [port] | --unbind | --status',
    'description': 'Handle client server'
  },
  'session': {
    'type': 'Shell',
    'usage': 'session --index [index]',
    'description': 'Establish a session with a client'
  },
  'delete': {
    'type': 'Shell',
    'usage': 'delete --index [index]',
    'description': 'Delete a connected client'
  },
  'break': {
    'type': 'Session',
    'usage': 'break',
    'description': 'Exit active session'
  },
  'uninstall': {
    'type': 'Session',
    'usage': 'uninstall',
    'description': 'Delete client file & exit'
  },
  'reconnect': {
    'type': 'Session',
    'usage': 'reconnect',
    'description': 'Reconnect a new client'
  },
  'cd': {
    'type': 'Session',
    'usage': 'cd --to [directory]',
    'description': 'Change directory of session shell'
  },
  'image': {
    'type': 'Session',
    'usage': 'image --screenshot | --cam (--monitor [index])',
    'description': 'Capture a screenshot / cam screenshot'
  },
  'upload': {
    'type': 'Session',
    'usage': 'upload --file [filename] | --url [url] (--execute)',
    'description': 'Upload file to client'
  },
  'download': {
    'type': 'Session',
    'usage': 'download --file [filename] (--execute)',
    'description': 'Download file from client'
  },
  'encrypt': {
    'type': 'Session',
    'usage': 'encrypt --file [filename] (--decrypt)',
    'description': 'Encrypt / decrypt a file'
  },
  'interpreter': {
    'type': 'Session',
    'usage': 'interpreter --execute [code] | --script [filename] (--quiet)',
    'description': 'Execute Python code'
  },
  'keylogger': {
    'type': 'Session',
    'usage': 'keylogger --run | --download (--quiet) | --close | --status',
    'description': 'Handle keylogger'
  },
  'keystroke': {
    'type': 'Session',
    'usage': 'keystroke --inject [inject] | --script [filename]',
    'description': 'Enumerate keyboard / mouse actions'
  },
  'persistence': {
    'type': 'Session',
    'usage': 'persistence --elevate | --schedule | --service',
    'description': 'Alternatives for client persistence'
  },
  'system': {
    'type': 'Session',
    'usage': 'system --shutdown | --restart | --logout | --standby',
    'description': 'Perform system actions'
  },
  'recover': {
    'type': 'Session',
    'usage': 'recover --password | --history (--force) (--quiet)',
    'description': 'Recover passwords / browser history'
  },
  'obfuscate': {
    'type': 'Session',
    'usage': 'obfuscate --logs',
    'description': 'Obfuscate forensic footprints'
  },
  'messagebox': {
    'type': 'Session',
    'usage': 'messagebox --title [title] --text [text] (--style [style])',
    'description': 'Display a messagebox'
  },
  'website': {
    'type': 'Session',
    'usage': 'website --open [open]',
    'description': 'Opens one or more websites'
  },
  'stream_2': {
    'type': 'Session',
    'usage': 'stream --resolution [resolution] (monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])',
    'description': 'Run stream module'
  },
  'cam_2': {
    'type': 'Session',
    'usage': 'cam --resolution [resolution] (--monitor [index]) (--fps) (--fit) (--ip [ip] & --port [port]) (--recognize [haarcascade])',
    'description': 'Run cam module'
  },
  'audio_2': {
    'type': 'Session',
    'usage': 'audio --run (--quiet) (--ip [ip] & --port [port])',
    'description': 'Run audio module'
  },
  'talk_2': {
    'type': 'Session',
    'usage': 'talk --run (--ip [ip] & --port [port])',
    'description': 'Run talk module'
  }
}


def get_help():
  all_commands = []
  for key, value in help_obj.items():
    all_commands.append([value['type'], value['usage'], value['description']])
  
  status_message(tabulate.tabulate(all_commands, headers=['Available', 'Usage', 'Description']), 'pure')