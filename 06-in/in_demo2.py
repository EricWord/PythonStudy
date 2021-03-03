word = 'hello'
x = input("请输入一个字符：")
if word.find(x) == -1:
    print("您输入的内容不存在！")
else:
    print("存在！")
