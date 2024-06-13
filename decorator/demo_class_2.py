import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        retval = self.func(*args, **kwargs)
        print(f"time: {time.time() - start}")
        return retval


@Timer
def sleep(x):
    time.sleep(x)


sleep(1)
