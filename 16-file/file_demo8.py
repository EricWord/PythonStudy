import json

file = open("names2.txt", "w", encoding="utf8")
# file.write("张三")
# write时，只能写入字符串或者二进制
# file.write(12)
# 类似字典、列表、数字等都不能直接写入到文件里

# 想要写入上述内容的话有两种方法：
# 第一种方法:将数据转换成为字符串 使用repr/str 更多的情况是使用json
# json的本质就是字符串，区别在于json里要使用双引号表示字符串
# 第二种方法:将数据转换称为二进制 使用pickle模块

names = ["张三", "tom", "jack", "lily"]
# json里将数据持久化有两个方法:
# dumps:将数据转换称为json字符串，不会将数据保存到文件里
# dump: 将数据转换称为json字符串的同时写入到指定的文件
# x = json.dumps(names, ensure_ascii=False)
# file.write(x)
json.dump(names, file, ensure_ascii=False)

# json反序列化也有两个方法:
# loads:将json字符串加载成为python里的数据
# load:读取文件，把读取的内容加载成为python里的数据
file.close()

# 符合json规则的字符串
x = '{"name":"张三","age":18}'
p = json.loads(x)
print(p, type(p))

# load读取一个文件，并把文件里的json字符串加载称为一个对象
file2 = open("names.txt", "r", encoding="utf8")
y = json.load(file2)
print(y)
print(y[0])
