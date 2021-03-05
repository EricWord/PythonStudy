# 运算符相关的魔法方法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return "hello"

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):  # 使用>=运算符时会自动调用
        pass

    def __le__(self, other):  # <=
        pass

    def __lt__(self, other):  # <
        pass

    def __add__(self, other):  # +
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):  # *
        pass

    def __truediv__(self, other):  # 做除法运算 /
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __int__(self):  # 调用int进行类型转换的时候会调用该方法
        pass

    def __float__(self):  # 调用float进行类型转换的时候会调用该方法
        pass


p1 = Person("张三", 19)
p2 = Person("张三", 19)
p3 = Person("李四", 20)
print(p1 is p2)
# ==运算符本质是调用对象的__eq__方法，获取__eq__的返回结果

print(p1 == p2)  # True
# != 本质是调用__ne__方法或者__eq__方法取反 not equal
print(p1 != p2)  # False

# 直接运行会报错
print(p1 > p3)
print(p1 + p2)
print(p1 - p2)

# 转换成字符串。默认会转换成为类型+内存地址
# str()将对象转换成字符串，会自动调用__str__方法
print(str(p1))  # <__main__.Person object at 0x110068080>
