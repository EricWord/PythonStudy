# 列表查询相关的方法
h = ["阿珂", "tom", "jack", "john", "tom"]
# 如果元素不存在，会报错
print(h.index("tom"))
print(h.count("tom"))
# in运算符
print("john" in h)
print("苏烈" in h)

# 使用下标可以直接修改列表中的元素
h[2] = "王霸"
print(h)
