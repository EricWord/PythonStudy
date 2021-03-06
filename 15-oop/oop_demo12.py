class Calcultor(object):
    # 静态方法
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b


print(Calcultor.add(1, 4))
print(Calcultor.minus(9, 2))


class Person:
    type = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # eat对象方法，可以直接使用实例对象.方法名(参数)调用
    # 使用对象名.方法名(参数)调用的方式，不需要传递self
    # 会自动将对象传递给self
    # 对象方法还可以使用 类对象来调用
    # 类名.方法名()
    # 这种方式不会自动给self传参，需要手动的指定
    def eat(self, food):  # 对象方法有一个参数self,指的是实例对象
        print(self.name + "正在吃" + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法定义成static
    @staticmethod
    def demo():  # 默认的方法都是对象方法
        print("hello")

    @classmethod
    def test(cls):  # 如果这个函数只用到了类属性，我们可以定义成一个类方法
        # 类方法有一个参数cls,也不需要手动传参，会自动传参
        # cls指定是类对象  cls == Person > True
        print("yes")


p = Person("张三", 18)
p2 = Person("李四", 19)
# 实例对象在调用方法时，不需要传self,会自动的把实例对象传递给self
p.eat("烧鸡")  # 直接使用实例对象调用方法

print(p.eat)
print(p2.eat)
print(p.eat is p2.eat)

print(Person.eat)
Person.eat(p2, "西红柿鸡蛋盖饭")

# 静态方法
Person.demo()
p.demo()

# 类方法可以使用实例对象和类对象调用
p.test()
Person.test()
