class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class X:
    pass


class Y:
    pass


class Student(Person, X):
    pass


p1 = Person("张三", 18)
p2 = Person("张三", 18)
s = Student("jack", 20)
# is是比较id(p1) 和 id(p2)
print(p1 is p2)  # is 身份运算符用来比较两个对象是否是同一个对象

# type(p1)获取的是类对象
if type(p1) == Person:
    print("p1是Person类创建的实例对象")

# isinstance用来判断一个对象是否是由指定的类(或者父类)实例化出来的
print(isinstance(s, Person))  # True
print(isinstance(s, (Student, Y)))  # True  # 有一个满足就返回True

# issubclass用来判断一个类是否是另一个类的子类
print(issubclass(Student, (Person, X)))  # True ,可以传多个，传多个父类的话需要使用元组
