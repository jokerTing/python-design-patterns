import time

'''
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)
'''
class Calculator(object):

    def fib_cached(self, n, cache):
        if n < 2:
            return 1
        try:
            result = cache[n]
        except:
            cache[n] = self.fib_cached(n-2, cache) + self.fib_cached(n-1, cache)
            result = cache[n]
        
        return result

if __name__ == "__main__":
    cal = Calculator()
    start_time = time.time()
    cache = {}
    fib_sequence = [cal.fib_cached(x, cache) for x in range(1, 40)]
    end_time = time.time()

    elapsed_time = (end_time - start_time)
    print("Time elapsed {}".format(elapsed_time))
    print(cache)
