import json

person = {"name": "zhangsan", "age": 19, "gender": "female"}
s = json.dumps(person)
print(s)
# 将json字符串转换为python里的数据
data = json.loads('{"name": "zhangsan", "age": 19, "gender": "female"}')
print(type(data))
