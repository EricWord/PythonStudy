# 字典遍历

person = {"name": "张三", "age": 18, "height": 190, "addr": "深圳"}
# 第一种遍历方式
for x in person:
    print(x, "=", person[x])
# 第二种方式：获取到所有的key，然后遍历key，根据key获取value
keys = person.keys()
print(type(keys))
for x in person.keys():
    print(x, "=", person[x])

# 第三种遍历方式：获取到所有的vlaue
for v in person.values():
    print(v)

# 第四种遍历方式
print("-----------")
print(person.items())
for item in person.items():
    print(item[0], "=", item[1])
# 第四种方式的等价方式
print("-----------")
for k, v in person.items():
    print(k, "=", v)
