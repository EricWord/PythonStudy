import re

# \s 表示任意的空白字符
print(re.search(r"\s", "hello world"))
# 换行
print(re.search(r"\n", "hello\nworld"))
# 制表符
print(re.search(r"\t", "hello\tworld"))

# \S 表示非空白字符
print(re.search(r"\S", "\t\n   x"))

# 标点符号的使用
# ():用来表示一个分组
# re.search(r"h()")

# 正则匹配一个括号里的内容(需要使用\)
m = re.search(r"\(.*\)", "(1+1)*3+5")
print(m.group())

# . 表示匹配除了换行以外的任意字符，如果想要匹配 . 需要使用 \.

# []用来表示可选项,[x,y] 从x到y区间，包含x和y
m2 = re.search(r"f[0-5]m", "pdsf6m")  # None
print(m2)
m3 = re.search(r"f[0-5]m", "pdsf3m")  # <re.Match object; span=(3, 6), match='f3m'>
print(m3)
# 匹配多个可选数字
m4 = re.search(r"f[0-5]+m", "pdsf34354m")  # <re.Match object; span=(3, 10), match='f34354m'>
print(m4)
# 可以出现字母
m5 = re.search(r"f[0-5a-d]m", "pdsfcm")  # <re.Match object; span=(3, 6), match='fcm'>
print(m5)
m6 = re.search(r"f[0-5a-dx]m", "pdsfxm")  # <re.Match object; span=(3, 6), match='fxm'>
print(m6)

print("-" * 20)
# | 用来表示或者 和[]有一定的相似，但是有区别
# 区别在于[]里的值表示的是区间，|就是可选值，可以出现多个值
m7 = re.search(r"f(x|prz|t)m", "pdsfprzm")
print(m7)

# {}用来限定出现的次数
# {n}:表示前面的元素出现n次
m8 = re.search(r"go{2}d", "good")
print(m8)
# {n,}:表示前面的元素出现n次以上
m9 = re.search(r"go{2,}d", "goooood")
print(m9)
# {,n}:表示前面的元素出现的次数≤n
m10 = re.search(r"go{,3}d", "goood")
print(m10)

# *：表示前面的元素出现任意次数(0次以以上)，等价于{0,}
print(re.search(r"go*d", "goood"))
# +:表示前面的元素至少出现一次，等价于{1,}

print(re.search(r"go+d", "god"))

# ?:两种用法:
# 1.规定前面的元素最多只能出现一次，等价于 {,1}
# 2.将贪婪模式转换为非贪婪模式
print(re.search(r"go?d", "gd"))
print(re.search(r"go?d", "god"))

# ^ 表示以指定的内容开头，$ 表示以指定的内容结尾
print(re.search(r"^a.*i$", "gj\najafsjswdlgi\ndkdsk", re.M))
