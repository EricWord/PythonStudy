class Student(object):
    __slots__ = ("name", "age", "city")  # 这个属性直接定义在类里，是一个元组，用来规定对象可以存在的属性

    def __init__(self, x, y):
        self.name = x
        self.age = y

    def say_hello(self):
        print("大家好，我是", self.name)


# Student("张三",18)到底做了什么?
# 1. 调用__new__方法，用来申请内存空间
# 2. 调用__init__方法，并让self指向申请好的那段内存空间，填充数据
# 3. 变量s1也指向创建好的那段内存空间
s = Student("张三", 18)
# 没有的属性，会报错
# print(s.height)

# 直接使用等号给一个属性赋值
# 如果这个属性以前不存在，会给对象添加一个新的属性
# 动态属性
s.city = "上海"  # 给对象添加了city属性
print(s.city)

# 如果这个属性以前存在，会修改这个属性对应的值
s.name = "jack"
print(s.name)
