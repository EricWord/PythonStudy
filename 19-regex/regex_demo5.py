import re

# 正则修饰符是对正则表达式进行修饰
# .表示除了换行以外的任意字符
# re.S 让.匹配换行
# re.I 忽略大小写
m = re.search(r"m.*a", "o3rjomo\njadas", re.S)
print(m)
print("-" * 20)
y = re.search(r"x", "good Xyz", re.I)
print(y)
# \w:表示的是字母数字和_
# +:出现一次以上
# $:以指定内容结尾
# re.M 让$能够匹配到换行
z = re.findall(r"\w+$", "i am boy\n you are girl\n he is man", re.M)
print(z)
