names = {"zhangsan", "lisi", "zhangsan", "wangwu", "zhaoliu"}
# set不能进行删改查
names.add("jack")
print(names)
names.pop()
print(names)

# 删除指定的元素
names.remove("jack")  # 如果key不能存在会报错
print(names)
# 清空set
# names.clear()
names.update({"刘能", "赵四"})
print(names)
