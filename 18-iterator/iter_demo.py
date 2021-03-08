from collections.abc import Iterable


class Demo:
    def __init__(self, x):
        self.x = x
        self.count = -1

    def __iter__(self):  # 只要重写了了__iter__方法就是一个可迭代对象
        return self

    def __next__(self):
        self.count += 1
        if self.count < self.x:
            # 每一次for...in都会调用一次__next__方法，获取返回值
            return self.count
        else:
            raise StopIteration  # 让迭代器停止


d = Demo(100)
print(isinstance(d, Iterable))

# for ... in 循环的本质就是调用可迭代对象的__iter__方法，获取到这个方法的返回值
# 这个返回值是一个迭代器对象，然后再调用这个对象的__next__方法
# for i in d:
#     print(i)

# 内置函数iter可以获取到一个可迭代对象的迭代器
i = iter(d)
print(next(i))
print(next(i))
print(next(i))
