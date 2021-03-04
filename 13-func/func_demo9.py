# 高阶函数
def outer():
    m = 100

    def inner():
        n = 90
        print("我是inner函数")

    print("我是outer函数")
    # 注意下面这行代码的inner后面不要加括号
    return inner


outer()()


def test():
    print("我是test函数")
    return "hello"


def demo():
    print("我是demo函数")
    return test()


def bar():
    print("我是bar函数")
    return test()


a = bar()
print(a)
x = demo()
print(x)
