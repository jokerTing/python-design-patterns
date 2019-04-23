class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)  

    instance = None

    def __new__(cls,*args, **kwargs):
        print("new")
        if not SingletonObject.instance:
            print("first create")
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        print("__getattr__() is called ")
        #return name + " from getattr"
        return getattr(self.instance, name)

    def __setattr__(self, name, val):
        print ("change")
        return setattr(self.instance, name , val) 