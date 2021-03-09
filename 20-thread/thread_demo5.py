# 多进程的使用
import multiprocessing, time


def dance(n):
    for i in range(n):
        time.sleep(0.5)
        print("正在跳舞")


def sing(m):
    for i in range(m):
        time.sleep(0.5)
        print("正在唱歌")


# 创建了两个进程
# target 用来表示执行的任务
# args 用来传参，类型是一个元组
p1 = multiprocessing.Process(target=dance, args=(20,))
p2 = multiprocessing.Process(target=sing, args=(50,))

p1.start()
p2.start()
