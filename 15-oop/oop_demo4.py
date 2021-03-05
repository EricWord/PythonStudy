import time


# 魔法方法，也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1. 不需要手动调用，会在合适的时机自动调用
# 2. 这些方法都是使用__开始，使用__结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用


class Person(object):
    # 在创建对象时会自动调用这个方法
    def __init__(self, name, age):
        print("__init__方法被调用了")
        self.name = name
        self.age = age

    # 当对象被销毁时会自动调用该方法
    def __del__(self):
        print("__del__方法被调用了")

    def __repr__(self):
        return "hello"

    def __str__(self):
        return "姓名:{},年龄:{}".format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print("__call__方法被调用了")
        #         args是一个元组，保存了(1,2)
        print("args={},kwargs={}".format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0], args[1])


p = Person("张三", 19)
# time.sleep(10)
# 如果不做任何修改，直接打印一个对象，是文件的__name__.类型 内存地址
# 当打印一个对象的时候，会调用这个对象的__str__或者__repr__方法
# 如果两个方法都写了，会走__str__
print(p)  # <__main__.Person object at 0x10eb1f9e8>
# print(repr(p))  # 调用内置函数repr,会触发对象的__repr__方法
# print(p.__repr__()) # 魔法方法一般不手动调用

# p()  # 对象名() 是调用对象的__call__方法，如果__call__方法没写会报错
# 可以传入参数
print(p(1, 2, fn=lambda x, y: x + y))
