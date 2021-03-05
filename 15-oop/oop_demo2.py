class Student(object):
    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print("大家好，我是", self.name)


# Student("张三",18)到底做了什么?
# 1. 调用__new__方法，用来申请内存空间
# 2. 调用__init__方法，并让self指向申请好的那段内存空间，填充数据
# 3. 变量s1也指向创建好的那段内存空间
s1 = Student("张三", 18)
s2 = Student("jack", 21)
s2.say_hello()
