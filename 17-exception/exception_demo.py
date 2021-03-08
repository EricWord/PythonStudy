def div(a, b):
    return a / b


try:
    x = div(5, 0)
    print("这里会打印吗")# 如果上一行代码出现异常，这行不会打印
except Exception as e:
    print("程序出错额")
else:
    print("计算的结果是", x)
