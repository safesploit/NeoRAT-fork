import getpass
import os


def client_root():
	user = getpass.getuser()
	drive = 'C'
	
	paths = {
		f'{drive}:\\Users\\{user}\\AppData\\Roaming',
		f'{drive}:\\Users\\{user}\\AppData\\Local',
		f'{drive}:\\Users\\{user}',
		os.getcwd()
	}

	for path in paths:
		if os.path.isdir(path):
			return path