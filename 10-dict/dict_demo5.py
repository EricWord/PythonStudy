# 字典推导式
dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)  # {100: 'a', 200: 'b', 300: 'c'}
# 字典推导式
dict3 = {v: k for k, v in dict1.items()}
print(dict3) # {100: 'a', 200: 'b', 300: 'c'}
