import abc

class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return 

class ConcreteFactory(AbstractFactory):
    def make_object(self):
        # do something
        return ConcreteClass()
        