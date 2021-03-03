# 列表的复制
x = [100, 200, 300]
# x和y指向了同一个内存空间，两者会相互影响
# 等号在这里表示内存地址的赋值
y = x
# x[0] = 1
print(y)

z = x.copy()
x[0] = 1
print(z)

# 除了使用列表自带的copy方法外，还可以使用copy模块实现拷贝
import copy

a = copy.copy(x)
print(a)

# 切片其实就是一个浅拷贝
names1 = ["张三", "李四", "王五", "杰克"]
names2 = names1[::]
names1[0] = "jerry"
print(names2)
