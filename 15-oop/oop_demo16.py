class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000

    def eat(self):
        print(self.name + "正在吃东西")

    # 父类的私有方法不会被子类继承，但是子类可以通过子类对象名._父类名__私有方法名()
    def __test(self):
        print("我是Animal类里的test方法")


class Person(Animal):
    pass


p = Person("张三", 18)
print(p.name)
p.eat()
