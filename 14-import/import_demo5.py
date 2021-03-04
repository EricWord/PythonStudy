import random

# randint(a,b) 用来生成[a,b]之间的整数
print(random.randint(2, 9))
# 生成[0,1)的随机浮点数
print(random.random())
# 生成[a,b)随机整数
print(random.randrange(2, 9))

# choice 用来在可迭代对象里随机抽取一个数据
print(random.choice(["张三", "李四", "王五", "赵丽", "jack"]))
# sample用来在可迭代对象里随机抽取n个数据
print(random.sample(["张三", "李四", "王五", "赵丽", "jack"], 2))
