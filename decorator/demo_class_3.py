import time


class Timer:
    def __init__(self, iteration):
        self.iteration = iteration

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(self.iteration):
                func(*args, **kwargs)
            print(f"time: {time.time() - start}")
        return wrapper


@Timer(3)
def sleep(x):
    time.sleep(x)


sleep(1)
