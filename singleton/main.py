from logger import Logger
from singleton_object import SingletonObject

if __name__ == '__main__':

    """
    logger_obj = Logger("design_patterns.log")
    logger_obj.info("This is an info message")
    """

    logger_obj1 = Logger(file_name="design_patterns.log")
    logger_obj1.info("This is an info message")
    print ("print obj1: ", logger_obj1)
    print ("-----")

    logger_obj2 = Logger("design_patterns_NEW.log")
    logger_obj2.error("This is an error message")
    print ("print obj1: ", logger_obj1)
    print ("print obj2: ", logger_obj2)
    print ("-----")
