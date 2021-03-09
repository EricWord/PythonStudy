import re

# 在python的正则表达式里，默认是贪婪模式，尽可能多的匹配

# 在贪婪模式后面添加?可以将贪婪模式转换成为非贪婪模式

m1 = re.search(r"m.*a", "o3rjomjadas")
print(m1)  # <re.Match object; span=(5, 10), match='mjada'>

m2 = re.search(r"m.*?a", "o3rjomjadas")
print(m2) # <re.Match object; span=(5, 8), match='mja'>

