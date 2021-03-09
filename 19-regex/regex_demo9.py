import re

# 正则表达式练习
# 判断用户输入的内容是否是数字，如果是数字转换成为数字类型
num = input("请输入一个数字:")
if re.fullmatch(r"\d+(\.?\d+)?", num):
    print("是个数字")
    print(float(num))
else:
    print("不是一个数字")
