names1 = {"zhangsan", "lisi"}
names2 = {"zhangsan", "wangwu", "zhaoliu"}
# 求差集
print(names2 - names1)  # {'zhaoliu', 'wangwu'}
# 求交集
print(names2 & names1)  # {'zhangsan'}
# 求并集
print(names2 | names1)  # {'wangwu', 'lisi', 'zhaoliu', 'zhangsan'}
# 求差集的并集
print(names2 ^ names1)  # {'lisi', 'zhaoliu', 'wangwu'}
