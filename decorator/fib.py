import time

def fib(n):
    if n < 2:
        return 
    fibPrev = 1
    fib = 1

    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib

def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print("[Time elapsed for n = {}] {}".format(n, end_time-start_time))
    return result

def get_profile_function(f):
    return lambda n: profile_me(f, n)

if __name__ == "__main__":
    n = 77
    fib_profiled = get_profile_function(fib)
    print("Fibonacci number for n = {}: {}".format(n, fib_profiled(n)))

