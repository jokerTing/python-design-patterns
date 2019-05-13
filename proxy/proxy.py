import time

class RawClass(object):
    def func(self, n):
        return f(n)

class memoize(fn):
    __cache = {}
    def memoized(*args):
        key = (fn.__name__, args)
        if key in __cache:
            return __cache[key]
        __cache[key] = fn(*args)
        return __cache[key]
    return memoized

class ClassProxy(object):
    def __init__(self, target):
        self.target = target
        func = getattr(self.target, 'func')
        setattr(self.target, 'func', memoize(func))
    def __getattr__(self, name):
        return getattr(self.target, name)