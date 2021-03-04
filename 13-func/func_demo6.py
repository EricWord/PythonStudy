# filter方法中使用匿名函数
# filter:对可迭代对象进行过滤
ages = [12, 23, 30, 17, 16, 22, 19]
# 两个参数：第一个是函数，第二个是可迭代对象
res = filter(lambda ele: ele > 19, ages)

for i in res:
    print(i)
