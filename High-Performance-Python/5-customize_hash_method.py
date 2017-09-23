# 默认的 hash 对于自定义对象的比较仅仅是使用内建的 id 函数返回对象在内存中的位置， __cmp__ 操作符比较的也是对象在内存中位置的数字值
# 这么做一般没问题，但是如果我们希望用 set 或 dict 对象来消除项目之间的歧义，默认函数就做不到了


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y


point1 = Point(1, 1)
point2 = Point(1, 1)
print({point1, point2})
# set([point1, point2]) == {point1, point2}


class SeniorPoint(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


senior_point1 = SeniorPoint(1, 1)
senior_point2 = SeniorPoint(1, 1)
print({senior_point1, senior_point2})
