word = 'hello'
x = input("请输入一个字符：")
# 判断用户输入的字符在字符串里是否存在
for c in word:
    if x == c:
        print("你输入的内容存在！")
        break
else:
    print("不存在")
