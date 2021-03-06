import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性 以两个_开始
        self.__money = 1000

    def test(self):
        self.__money += 10  # 在这里可以访问私有属性

    def get_money(self):
        print("{}查询了余额".format(datetime.datetime.now()))
        return self.__money

    def set_money(self, mon):
        if type(mon) != int:
            print("格式非法！")
            return
        print("{}修改了余额".format(datetime.datetime.now()))
        self.__money = mon

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print("我是__demo,name={}".format(self.name))


p = Person("张三", 18)
# p.__money # 不能直接获取到私有变量

# 获取私有变量的方式：
# 方式1. 使用 对象._类名_私有变量名获取
print(p._Person__money)  # 通过这种方式也能获取到私有属性

p.test()
print(p._Person__money)

# 方式2. 定义get和set方法来获取
print(p.get_money())
p.set_money("hello")
print(p.get_money())
# p.__demo() # 调用私有函数报错，但是可以通过下面这种方式调用私有函数
p._Person__demo()
# 方式3. 使用property()来获取
