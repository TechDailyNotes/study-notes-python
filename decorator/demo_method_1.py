import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        retval = func(*args, **kwargs)
        print(f"time: {time.time() - start}s")
        return retval
    return wrapper


@timeit
def sleep(x):
    time.sleep(x)


sleep(1)
