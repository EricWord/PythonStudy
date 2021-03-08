# with我们称之为上下文管理器，很多需要手动关闭的连接
# 比如说 文件连接、socket连接、数据库的连接、都能使用with关键字自动关闭连接
# with关键字后面对象，需要实现__enter__和__exit__魔法方法
# 当进入到with代码块时，会自动调用__enter__方法里的代码
# 当with代码块执行完成以后，会自动调用__exit__方法

class Demo(object):
    pass

    def __enter__(self):
        print("__enter__方法被执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__方法被调用了")


def create_obj():
    x = Demo()
    return x


with create_obj() as d:
    # 变量d不是create_obj的返回结果，它是创建的对象x调用__enter__之后的返回结果
    print(d)
