import re

# 正则表达式规则
# 1.数字和字母都表示它本身
re.search(r"x", "hello xyz")
re.search(r"5", "r353720")
# 2. 很多字母前面添加\会有特殊含义

print(re.search(r"d", "good"))
#  \d有特殊含义，不再表示字母d
print(re.search(r"\d", "good"))
print(re.search(r"\d", "goods8085823d"))

# 3. 绝大多数标点符号都有特殊含义
# re.search("+","1+2") 不能直接使用，+有特殊含义

# 4. 如果想要使用+ ，需要加\
m2 = re.search("\+", "1+2")
print(m2)
