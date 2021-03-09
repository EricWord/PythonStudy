import re

# 可以直接调用re.search方法
m = re.search(r"m.*a", "o3rjomjadas")
print(m)
r = re.compile(r"m.*a")
x = r.search("o3rjomjadas")
print(x)
