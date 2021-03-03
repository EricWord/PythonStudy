# 字典的增删改
person = {"name": "张三", "age": 18, "height": 190, "age": 22}

# 修改
person["name"] = "李四"
print(person)
# 增加
person["gender"] = "female"
print(person)

# 把name对应的键值对删除
# pop的返回值是key对应的value
res1 = person.pop("name")
print("res1=", res1)  # res1= 李四
print(person)
# popitem的返回值是元组
res = person.popitem()
print(person)
print(res)  # ('gender', 'female')

# 清空字典
person.clear()
print(person)
