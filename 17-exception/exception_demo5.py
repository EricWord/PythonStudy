try:
    with open("../16-file/xxx.txt", "r") as file:
        file.read() #这里不需要再手动关闭文件，with关键字会帮助我们关闭文件

except FileNotFoundError:
    print("文件未找到")

# with我们称之为上下文管理器，很多需要手动关闭的连接
# 比如说 文件连接、socket连接、数据库的连接、都能使用with关键字自动关闭连接
# with关键字后面对象，需要实现__enter__和__exit__魔法方法

