# dis 模块是内建的，你可以传给它一段代码或者一个模块，它会打印出分解的字节码。
import dis


def fn_expressive(upper = 1000000):
    total = 0
    for n in range(upper):
        total += n
    return total


def fn_terse(upper = 1000000):
    return sum(range(upper))


if __name__ == '__main__':
    print("functions return the same result: ", fn_expressive() == fn_terse())

    print(fn_expressive.__name__)
    dis.dis(fn_expressive)

    print(fn_terse.__name__)
    dis.dis(fn_terse)
