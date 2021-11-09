from foreign.utility.device_support import *
from foreign.utility.location_data import *
from foreign.utility.system_info import *


def connection_data(silent, io_channels, extra_data):
	connection_data_obj = {}

	connection_data_obj.update(device_support(silent, io_channels))
	connection_data_obj.update(system_info(extra_data))
	connection_data_obj.update(location_data())

	return connection_data_obj