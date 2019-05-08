import time
'''
import abc
class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, observed): pass
    
class ConcreteObserver(Observer):
'''
class ConcreteObserver(object):
    def update(self, observed):
        print("Observing: {}".format(observed))

class Observable(object):
    def __init__(self):
        self.callbacks = set()
        self.changed = False
    
    def register(self, observer):
        self.callbacks.add(observer)
    
    def unregister(self, observer):
        self.callbacks.discard(observer)

    def unregister_all(self):
        self.callbacks = set()
    
    def poll_for_change(self):
        if self.changed:
            self.update_all
    
    def update_all(self):
        for callback in self.callbacks:
            callback(self)

def main():
    observerd = Observable()
    observer1 = ConcreteObserver()
    observerd.register(lambda x:observer1.update(x))
    # observerd.update_all()
    #while True:
    for _ in range(10):
        time.sleep(3)
        observerd.poll_for_change()

if __name__ == "__main__":
    main()