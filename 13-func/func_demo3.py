# 匿名表达式
# fn = lambda a, b: a + b
# print(fn(3, 4))

def calc(a,b,fn):
    return fn(a,b)

# 将匿名函数传给calc
print(calc(3, 5, lambda a, b: a + b))
print(calc(3, 5, lambda a, b: a - b))
print(calc(3, 5, lambda a, b: a * b))
print(calc(3, 5, lambda a, b: a / b))