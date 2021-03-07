import os

# 文件拷贝
file_name = input("请输入一个文件路径:")
# 判断是否是文件
if os.path.isfile(file_name):
    # 打开旧文件
    # 指定模式为rb的原因是如果读取的不是文本文件，会报错
    old_file = open(file_name, "rb")
    # 第一种方式 使用rpartition
    # names = file_name.rpartition(".")
    # new_file_name = names[0] + ".bak." + names[2]
    # 第二种方式 使用splittext
    names = os.path.splitext(file_name)
    new_file_name = names[0] + ".bak" + names[1]
    # 打开一个新文件用于写入
    # 以二进制的形式读，以二进制的形式写
    new_file = open(new_file_name, "wb")
    while True:
        content = old_file.read(1024)
        # 把旧文件中的数据读取出来写入到新文件
        new_file.write(content)
        if not content:
            break
    new_file.close()
    old_file.close()
else:
    print("您输入的文件不存在")
