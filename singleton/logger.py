from singleton_object import SingletonObject
#record the log
#__author__='ShadowDing'

class Logger(object):
    """
    A file-based message logger with the following properties

    Attributes:
        file_name: a string representing the full path of the log file to which 
    this logger will write its messgae
    """
    class __Logger():

        def __init__(self, file_name):
            """ Return a Logger object whose file_name is *file_name* """
            self.file_name = file_name
        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)  

        # record msg in the Target file
        def _write_log(self, level, msg):
            with  open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1} \n".format(level, msg))

        # record the CRITICAL msg
        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        # record the ERROR msg
        def error(self, msg):
            self._write_log("ERROR", msg)

        # record the WARN msg
        def warn(self, msg):
            self._write_log("WARN", msg)

        # record the INFO msg
        def info(self, msg):
            self._write_log("INFO", msg)

        # record the DEBUG msg
        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls, *args, **kwargs):
        print("new")
        if not Logger.instance:
            print("first create")
            Logger.instance = Logger.__Logger(*args, **kwargs)
        return Logger.instance

    def __getattr__(self, name):
        print("__getattr__() is called ")
        #return name + " from getattr"
        return getattr(self.instance, name)

    def __setattr__(self, name, val):
        print ("change")
        return setattr(self.instance, name , val) 
