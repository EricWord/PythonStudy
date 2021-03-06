# mode指的是文件的打开方式
# r:只读模式，默认,如果文件不存在会报错
# w:写入模式，打开文件后只能写入，不能读取，如果文件存在，会覆盖文件，如果文件不存在，会创建
# b:以二进制的形式打开文件
# rb:以二进制读取
# wb:以二进制写入
# a:追加模式，如果文件不存在会创建文件
# r+:可读写，文件不存在会报错
# w+:可读写，文件不存在会创建，存在会覆盖


# file = open("xxx.txt", "r")
# print(file.read())
# file.write("hello")

# file = open("xxx.txt", "w")
# file = open("yyy.txt", "w")

# print(file.read()) # io.UnsupportedOperation: not readable
# file.write("hello")

file = open("xxx.txt", "rb")
print(file.read())
file.close()
