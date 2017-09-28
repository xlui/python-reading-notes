# 每当 Python 访问一个变量、函数或模块时，都有一个体系来决定它去哪里查找这些对象。
# 首先，Python 查找 locals() 数组，其内保存了所有本地变量的条目。Python 花了很多精力优化本地变量的查询速度，这也是整条链上唯一不需要
# 字典查询的部分
# 如果不在本地变量里，那么会搜索 globals() 字典。
# 最后，如果也不在 globals() 里，则搜索 __builtin__ 对象（其实是搜索 __builtin__ 的 locals() 字典，对所有模块对象和类对象也一样）。

# 下面这个例子展现了 namespace 的不同导致的速度提升
from time import time
from functools import wraps
from math import sin


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
def tight_loop_slow(iterations):
    result = 0
    for i in range(iterations):
        result += sin(i)


@time_fn
def tight_loop_fast(iterations):
    result = 0
    local_sin = sin
    for i in range(iterations):
        result += local_sin(i)


iteration_times = 10000000
tight_loop_slow(iteration_times)
tight_loop_fast(iteration_times)
# test failed!!!! the function tight_loop_fast takes much more time than function tigth_loop_slow
