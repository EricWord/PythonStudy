# map中匿名函数的使用
ages = [12, 23, 30, 17, 16, 22, 19]
# 把列表中的每个元素都加2
res = map(lambda ele: ele + 2, ages)
print(list(res))
