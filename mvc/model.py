import os
import datetime

class NameModel(object):
    def __init__(self):
        self.filename = 'names.dat'
    
    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'
    
    def get_name_list(self):
        if not os.path.exists(self.filename):
            return False
        with open(self.filename, 'r') as data_file:
            names = data_file.read().split('\n')
        return names
    
    def save_name(self, name):
        with open(self.filename, self._get_append_write()) as data_file:
            data_file.write("{}\n".format(name))

class TimeModel(object):
    def __init__(self):
        pass
    
    def get_time_of_day(self):
        time = datetime.datetime.now()
        if time.hour < 12:
            return "Morning"
        if 12 <= time.hour < 18:
            return "afternoon"
        if time.hour >= 18:
            return "evening"