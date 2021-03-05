class Person(object):
    __slots__ = ("name", "age", "__dict__")
    '''
    这是一个人类
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭")


p = Person("张三", 18)
# 查看对象所有的属性和行为
print(dir(p))
print(p.__class__)  # <class '__main__.Person'>
# 把对象属性和值转换成为一个字典
print(p.__dict__)  # {'name': '张三', 'age': 18}
print(p.__dir__())  # 等价于dir(p)
print(p.__doc__)  # 也可以直接使用类名调用
print(Person.__doc__)
# print(range.__doc__)
print(p.__module__)  # 模块名
print(p.__slots__)
