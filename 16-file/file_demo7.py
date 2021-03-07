import sys

# sys.stdin 接收用户输入
# sys.stdout 标准输出
# sys.stderr 错误输出

# stdin = sys.stdin
# while True:
#     content = stdin.readline()
#     if content == '\n':
#         break
#     print(content)

sys.stdout = open("stdout.txt", "w", encoding="utf8")
print("hello")

sys.stderr = open("stderr.txt", "w", encoding="utf8")
print(1 / 0)
