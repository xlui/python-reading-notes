# 利用 Decorator 而不是简单的 print 语句来测量 python 函数运行时间
from time import time
from functools import wraps


def time_fn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        time_start = time()
        result = fn(*args, **kwargs)
        time_end = time()
        print("@time_fn: function", fn.__name__, "took", (time_end - time_start), "seconds")
        return result
    return measure_time


@time_fn
def t():
    print("Hello World")


if __name__ == '__main__':
    t()
