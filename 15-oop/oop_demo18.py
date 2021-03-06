class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + "正在睡觉")


class Student(Person):
    def __init__(self, name, age, school):
        # 调用父类方法方式1
        super().__init__(name, age)
        # 调用父类方法方式2
        # Person.__init__(name,age)
        self.school = school

    def study(self):
        print(self.name + "正在学习")

    def sleep(self):
        print(self.name + "正在课间休息时睡觉")


# 调用了父类的__init__方法
s = Student("jerry", 20, "川田")
# 调用了父类的sleep方法
s.sleep()

print(Student.__mro__)  # method resolution order

# 1. 子类的实现与父类的实现完全不一样，子类可以选择重写父类的方法
# 2. 子类在父类的基础上又有更多的实现
