# 运算符相关的魔法方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print("__eq__方法被调用")
        return self.name == other.name and self.age == other.age


p1 = Person("张三", 18)
p2 = Person("张三", 18)

print("p1 addr:0x%X" % id(p1))
print("p2 addr:0x%X" % id(p2))

# is 身份运算符可以用来判断两个对象是否是同一个对象
print("p1 is p2", p1 is p2)
print("p1 == p2", p1 == p2)
# is 比较两个对象的内存地址
# ==会调用对象的__eq__方法，获取这个方法的比较结果
# __eq__如果不重写，默认比较的依然是内存地址

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(nums1 is nums2)
print(nums1 == nums2)
