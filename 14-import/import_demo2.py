import os

print(os.name)
print(os.sep)
#  os里的path常用
# abspath 获取文件的绝对路径
print(os.path.abspath("import_demo2.py"))
#  判断是否是文件夹
print(os.path.isdir("import_demo2.py"))
# 判断是否是文件
print(os.path.isfile("import_demo2.py"))
# 判断是否存在
print(os.path.exists("import_demo2.py"))

file_name = "2021.03.04.demo.py"
print(os.path.splitext(file_name))
