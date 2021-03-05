class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setitem__(self, key, value):
        # print("__setitem__方法被调用,key={},value={}".format(key, value))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


p = Person("张三", 18)
# 将对象转换称为字典
print(p.__dict__)  # {'name': '张三', 'age': 18}

# 不能直接把一个对象当做字典来用,需要重写__setitem__方法
p["name"] = "jack"  # []语法会调用对象的__set_item__方法
print(p.__dict__)  # {'name': '张三', 'age': 18}
print(p["name"])  # 会调用__getitem__方法
