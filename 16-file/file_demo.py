# python里使用open内置函数打开并操作一个文件
# file:用来打开指定的文件(不是文件的名字，而是文件的路径)
# mode:打开文件的模式,默认是r，只读
# encoding:打开文件时的编码方式
# 返回值是打开文件的对象
file = open("xxx.txt")
print(file.read())

# 操作完成文件以后，关闭文件
file.close()
