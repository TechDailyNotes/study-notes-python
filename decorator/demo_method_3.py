import time


def timeit(iteration):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteration):
                func(*args, **kwargs)
            print(f"time: {time.time() - start}")
        return wrapper
    return inner


@timeit(3)
def sleep(x):
    time.sleep(x)


sleep(1)
