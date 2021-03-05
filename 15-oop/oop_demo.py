#  class 类名：类名需要遵守大驼峰命名，第一个单词的首字母大写
class Student(object):
    def __init__(self, name, age, height):  # 在__init__方法里，以参数的形式定义属性
        self.name = name
        self.age = age
        self.height = height

    #     行为定义为一个个函数
    def run(self):
        print("正在跑步")

    def eat(self):
        print("正在吃东西")


# Student() 会自动调用 __init__方法
# 使用Student类创建了两个实例对象s1 s2
# s1和s2都会有name,age,height属性,同时都有run和eat方法
s1 = Student("小明", 18, 175)
s2 = Student("小美丽", 17, 165)

# 根据业务逻辑，让不同的对象执行不同的行为
s1.run()
s1.eat()

s2.eat()
