import os

# 文件拷贝
file_name = input("请输入一个文件路径:")
# 判断是否是文件
if os.path.isfile(file_name):
    # 打开旧文件
    old_file = open(file_name)
    new_file_name = "test.txt"
    # 打开一个新文件用于写入
    new_file = open(new_file_name, "w")
    # 把旧文件中的数据读取出来写入到新文件
    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
else:
    print("您输入的文件不存在")
