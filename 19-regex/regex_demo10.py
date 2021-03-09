import re

# 替换
# sub
# 第一个参数是正则表达式
# 第二个参数是新字符
# 第三个参数是需要被替换的原来的字符串
# 将数字全部替换成x
print(re.sub(r"\d", "x", "sgdho7539hsfdl27r92h3h3l733h3lh"))
p = "hello34good23"


# 把字符串里的数字*2

def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


print("-" * 20)
# sub内部在调用test方法时，会把每一个匹配到的数据以re.Match的格式传参
print(re.sub(r"\d+", test, p))  # test函数是自动调用的
