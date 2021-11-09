import os

from domestic.global_state import *


def make_directories(directories):
	root = state['root']

	if not os.path.isdir(root):
		os.mkdir(root)

	for directory in directories:
		if not os.path.isdir(f'{root}/{directory}'):
			os.mkdir(f'{root}/{directory}')