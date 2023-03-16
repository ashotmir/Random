from time import sleep
from datetime import datetime


def profile(func):
    def time(*args):
        file = open("Timer", "a")
        start = datetime.now()
        res = func(*args)
        over = datetime.now() - start
        file.write(f"{str(start)} - {func.__name__}({str(*args)}) - {over}\n")
        file.close()
        return res

    return time


@profile
def foo(x):
    sleep(2)
    return print(x ** 2)


foo(2)
sleep(5)
foo(42)