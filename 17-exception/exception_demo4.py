def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return "除数不能为0"
    else:
        return x
    finally:
        return "good"  # 如果函数里有finally,finally里的返回值会覆盖之前的返回值


print(demo(1, 0))
