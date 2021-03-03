# 字典的查询
person = {"name": "张三", "age": 18, "height": 190, "age": 22}
print(person["name"])
print(person.get("sdfnlsd","默认值")) # 如果不存在会返回None
