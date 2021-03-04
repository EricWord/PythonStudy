import time


# 装饰器
def cal_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时", end - start)

    return inner


@cal_time  # 1.调用cal_time 2. 把被装饰的函数传给fn 3.再次调用demo已经不是原来的demo,而是cal_time的返回值inner
def demo():
    x = 0
    for i in range(1, 100000):
        x += i
    print(x)


demo()
