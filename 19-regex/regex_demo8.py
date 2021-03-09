import re

# 字母的特殊含义
# \n表示换行 \t:表示一个制表符 \s:空白字符 \S:非空白字符
# \d:表示数字，等价于[0-9]

print(re.search(r"x\d+p", "x243p"))  # <re.Match object; span=(0, 5), match='x243p'>

# \D:表示非数字，等价于[^0-9]
# ^ 除了表示以指定的内容开始以外，在[]里还可以表示取反
print("-" * 20)
print(re.search(r"\D+", "he110"))
print(re.search(r"[^0-9]+", "he110"))

# \w:表示数字、字母、_以及中文  等价于[0-9a-zA-Z_]还有中文
print(re.search(r"\w+", "hE110_X*.+-"))
print(re.findall(r"\w+", "大,家,好"))  # ['大', '家', '好']

# \W: \w取反
print(re.findall(r"\W+", "hE110_X*.+-"))
