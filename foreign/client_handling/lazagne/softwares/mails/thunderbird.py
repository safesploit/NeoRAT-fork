from foreign.client_handling.lazagne.config.module_info import ModuleInfo
from foreign.client_handling.lazagne.softwares.browsers.mozilla import Mozilla


class Thunderbird(Mozilla):

    def __init__(self):
        self.path = u'{APPDATA}\\Thunderbird'
        ModuleInfo.__init__(self, 'Thunderbird', 'mails')
