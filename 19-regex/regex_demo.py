# 正则表达式

import re

# 在正则表达式里，如果想要匹配一个\需要使用\\\\
x = "hello\\nworld"
# 第一个参数就是正则匹配规则
# 第二个参数表示需要匹配的字符串
# m = re.search("\\\\", x)
# 还可以在字符串前面加 r,此时\\就表示\
m = re.search(r"\\", x)
# search 和 match返回的结果是一个Match类型的对象
print(m)  # <re.Match object; span=(5, 6), match='\\'>
