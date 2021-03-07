# pickle:将python里任意的对象转换成为二进制
import pickle
import json

# 序列化 dumps: 将python里的数据转换成为二进制 dump:将python数据转换成为二进制，同时保存到指定文件
# 反序列化 loads:将二进制加载称为python里的数据 load:读取文件并将文件的内容加载成为二进制
names = ["张三", "李四", "杰克", "亨利"]
b_names = pickle.dumps(names)
# print(b_names)

file = open("names_bin.txt", "wb")
file.write(b_names)
file.close()

file2 = open("names_bin.txt", "rb")

x = file2.read()
y = pickle.loads(x)
print(y)

file3 = open("names_bin2.txt", "wb")
pickle.dump(names, file3)
file2.close()
file3.close()

file4 = open("names_bin2.txt", "rb")
load = pickle.load(file4)
print(load)
file4.close()


class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(self.name + "正在吃东西")


d = Dog("大黄", "白色")
# 保存到文件里
pickle.dump(d, open("dog.txt", "wb"))
# 从文件里加载出来
dd = pickle.load(open("dog.txt", "rb"))
print(dd.name)
dd.eat()

# 使用json把一个对象序列化
print(json.dumps(d.__dict__, ensure_ascii=False))
