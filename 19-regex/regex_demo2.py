# 正则查找相关的方法

import re

m = re.match(r"hello", "world hello good morning")
print(m)
m = re.search(r"hello", "world hello good morning")
print(m)

m2 = re.search("x", "sdgfjhsdlxxvsllxjlxjxgixguitxcvxgtix")
print(m2)
m3 = re.finditer("x", "sdgfjhsdlxxvsllxjlxjxgixguitxcvxgtix")
print(m3)

for t in m3:
    print(t)

print("-" * 10)
m4 = re.findall("x", "sdgfjhsdlxxvsllxjlxjxgixguitxcvxgtix")
print(m4)
