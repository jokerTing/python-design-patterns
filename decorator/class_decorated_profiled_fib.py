import time
from functools import wraps

def profiling_decorator_unit(unit):
    def ProfilingDecorator(f):

        @wraps(f)
        def wrap_f(*args):
            start_time = time.time()
            result = f(*args)
            end_time = time.time()
            if unit == "seconds":
                elapsed_time = (end_time - start_time) / 1000
            else:
                elapsed_time = end_time - start_time
            print("[Time elapsed for n = {}] {}".format(n, elapsed_time))
            return result
        return wrap_f
    return ProfilingDecorator

def ToHTMLDecorator(f):
    print("ToHMTLDecorator called")
    def HTML_f(*args):
        return "<html><body>{}</body></html>".format(f(*args)) 
    return HTML_f 

#@ToHTMLDecorator
@profiling_decorator_unit("seconds___")
def fib(n):
    if n < 2:
        return 
    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib

if __name__ == "__main__":
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))
