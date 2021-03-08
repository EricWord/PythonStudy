class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "长度必须要在{}至{}之间".format(self.x, self.y)


password = input("请输入您的密码：")
m = 6
n = 12
if m <= len(password) <= n:
    print("密码正确")
else:
    # 使用raise关键字抛出一个异常
    raise LengthError(m, n)

print("将密码保存到数据库")
