# 列表是用来保存多个数据的
# 操作列表 增删改查
h = ["阿珂", "tom", "jack", "john"]
print(h)
# append 在列表的最后添加元素
h.append("小红")
print(h)
# insert在指定index位置前面添加元素
h.insert(0, "numOne")
print(h)
x = ["马可波罗", "狄仁杰", "米莱迪"]
# extend 需要一个可迭代对象
# 把x添加到h里
h.extend(x)
print(h)
