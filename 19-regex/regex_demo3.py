import re

m = re.search(r"m.*a", "o3rjomjadas")
# 匹配到的结果字符串的开始和结束下标
print(m.span())
# 获取匹配的字符串结果
print(m.group())
# group方法表示正则表达式的分组
# 1.在正则表达式里使用()表示一个分组
# 2.如果没有分组，默认只有一组
# 3.分组的下标从0开始

# groupdict作用是获取到分组组成的字典

# (?P<name>表达式) 可以给分组起一个名字

# 通过名字获取到的是一个字典
# 通过下标获取到的匹配到的字符串