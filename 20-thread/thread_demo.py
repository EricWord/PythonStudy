import threading, time


def dance():
    for i in range(50):
        time.sleep(0.2)
        print("我正在跳舞")


def sing():
    for i in range(50):
        time.sleep(0.2)
        print("我正在唱歌")


# python里同时执行多个任务有以下几种方式:
# 1.多线程
# 2.多进程
# 3.多进程+多线程
# dance()
# sing()

# target需要的是一个函数，用来指定线程需要执行的任务
t1 = threading.Thread(target=dance)  # 创建了线程1
t2 = threading.Thread(target=sing)  # 创建了线程2

t1.start()
t2.start()
