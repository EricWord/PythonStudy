# 闭包
def outer():
    x = 10  # 局部变量

    def inner():
        # 在内部函数修改外部函数的局部变量
        nonlocal  x
        y = x + 1
        x=20

    return inner
