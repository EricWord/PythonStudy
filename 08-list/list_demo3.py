# 列表删除数据有3个相关的方法 pop remove clear
h = ["阿珂", "tom", "jack", "john"]
# pop会删除列表的最后一个元素
s = h.pop()
print(s)
print(h)
# pop(index)删除指定index的数据
h.pop(1)
print(h)
# 如果要删除的元素不存在，会报错
h.remove("jack")
print(h)

lis = ["阿珂", "tom", "jack", "john"]
print(lis)
# del删除指定位置的元素
del lis[2]
print(lis)
# clear用来清空一个列表
lis.clear()
print(lis)
