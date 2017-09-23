# 这个例子显示 list 和 tuple 存储方式不同导致的差异

# list 动态存储，每次添加元素仅当 list 长度不够会重新分配内存，分配公式为： M = (N >> 3) + (N < 9 ? 3 : 6)
# 当 list 的长度到了一个十分大的地步的时候，list 在内存中的实际占用可能会超乎想象的更大！

# tuple 静态存储，每次添加元素（合并成为新元组）都会有分配和复制的操作，但是 tuple 在内存中的占用始终是真实大小，没有额外占用！

# 例子： 一个使用 append 操作的大小为 1 0000 0000 的列表实际上占用了 1 1250 0007 的元素的内存
#       而保存同样数据的元组始终占用 1 0000 0000 个元素的内存

import timeit

t1 = timeit.Timer('l = [0,1,2,3,4,5,6,7,8,9]').timeit()
t2 = timeit.Timer('d = (0,1,2,3,4,5,6,7,8,9)').timeit()

print(t1)
print(t2)
print("Create a list is slow than a same tuple", t1 / t2, "times.")
