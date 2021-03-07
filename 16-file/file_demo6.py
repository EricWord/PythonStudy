# 将数据写入到内存涉及到StringIO和BytesIO两个类
from io import StringIO, BytesIO

str_io = StringIO()
# 把数据写入内存
# str_io.write("hello")
# str_io.write("good")

# print(str_io.getvalue())

print("yes", str_io)
print("ok", str_io)
print(str_io.getvalue())

str_io.close()

b_io = BytesIO()
b_io.write("你好".encode("utf8"))
print(b_io.getvalue().decode("utf8"))

b_io.close()
