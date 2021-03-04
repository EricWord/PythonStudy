# 计算一段代码的执行时间
import time
start =time.time()
x = 1
for i in range(1, 20):
    x *= i

print(x)
end = time.time()
print(end-start)
