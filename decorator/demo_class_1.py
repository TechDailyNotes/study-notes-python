import time


class Timer:
    def timeit(iteration):
        def inner(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                for _ in range(iteration):
                    retval = func(*args, **kwargs)
                print(f"time: {time.time() - start}")
                return retval
            return wrapper
        return inner

    @timeit(2)
    def sleep(self, x):
        time.sleep(2 * x)

    timeit = staticmethod(timeit)


timer = Timer()


@timer.timeit(3)
def sleep(x):
    time.sleep(x)


sleep(1)
timer.sleep(1)
