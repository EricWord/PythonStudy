class Person(object):
    type = "人类"  # 这个属性定义在类里，函数之外，我们称之为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


# p是通过Person创建出来的实例对象
# name和age是对象属性，在__init__方法里以参数的形式定义的，是每个实例对象都会单独保存一份的属性
# 每个实例对象之间的属性没有关联，互不影响
p1 = Person("张三", 18)
p2 = Person("李四", 19)

# 类属性可以通过对象和实例对象获取
print(Person.type)  # 通过类对象获取类属性
print(p1.type)  # 通过实例对象来获取类属性

# 类属性只能通过类对象来修改，实例对象无法修改类属性
p1.type = "human"
print(p1.type)  # 此处并没有修改类属性，只是给p1加了一个type属性
print(Person.type)

Person.type = "宇宙超人"
print(p2.type)  # 类属性已经修改
print(Person.type)
