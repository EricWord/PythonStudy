class Singleton(object):
    __instance = None  # 类属性
    __is_first = True

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 申请内存，创建一个对象，并把对象的类型设置为cls

        return cls.__instance


# 如果不重写 __new__方法，会调用object的__new__方法
# object的__new__方法会申请内存
# 如果重写了__new__，需要手动申请内存
s1 = Singleton("呵呵呵", "嘿嘿嘿")
s2 = Singleton("哈哈哈", "噗噗噗")
print(s1 is s2)
print(s2.a, s2.b)
