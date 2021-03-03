# 列表推导式是使用简单的语法创建一个列表

nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2 == 0]
print(x)

points = [(x1, y1) for x1 in range(5, 7) for y1 in range(10, 13)]
print(points)
