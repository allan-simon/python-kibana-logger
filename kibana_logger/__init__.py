'''
Module to easily get application logs into kibana
'''

import syslog
import json

__version__ = (0, 2, 0)

class KibanaLogger(object):
    '''Object to ease json-logging with syslog-compatible system
    It uses the CEE token format, so that it can be used by rsyslog
    to feed the messages directly to kibana

    In order to avoid repeating again and again the same keys
    it is possible to define some preset keys/values
    '''
    CEE = "@cee: "

    def __init__(self, preset=None):
        syslog.openlog(facility=syslog.LOG_LOCAL7)
        if preset is None:
            preset = {}
        self.preset = preset

    def clone_with(self, more_preset):
        '''create new instance with more presets
        '''
        new_preset = self._merge_with_preset(more_preset)
        return self.__class__(new_preset)

    def new_with(self, more_preset):
        '''create new instance with more presets
        WARNING: deprecated, please use clone_with
        '''
        new_preset = self._merge_with_preset(more_preset)
        return self.__class__(new_preset)

    def update_in_place(self, more_preset):
        '''Add some presets to the current instance ones.
        Use this method wisely as it alters the current instance
        '''
        self.preset.update(more_preset)

    def _merge_with_preset(self, data):
        '''merge preset with given data
        '''
        # we create a new dictionnary to avoid
        # modifying self.preset, as we want to keep
        # it intact for further call
        all_data = {}
        all_data.update(self.preset)
        all_data.update(data)
        return all_data

    def _create_syslog_string(self, data):
        all_data = self._merge_with_preset(data)
        text = (self.CEE + json.dumps(all_data))
        return text

    def info(self, data):
        '''log data + preset as info message
        '''
        text = self._create_syslog_string(data)
        syslog.syslog(syslog.LOG_INFO, text)

    def warning(self, data):
        '''log data + preset as warning message
        '''
        text = self._create_syslog_string(data)
        syslog.syslog(syslog.LOG_WARNING, text)

    def error(self, data):
        '''log data + preset as error message
        '''
        text = self._create_syslog_string(data)
        syslog.syslog(syslog.LOG_ERR, text)

    def debug(self, data):
        '''log data + preset as debug message
        '''
        text = self._create_syslog_string(data)
        syslog.syslog(syslog.LOG_DEBUG, text)

    def critical(self, data):
        '''log data + preset as critical message
        '''
        text = self._create_syslog_string(data)
        syslog.syslog(syslog.LOG_CRIT, text)
