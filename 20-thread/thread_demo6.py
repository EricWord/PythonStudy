# 进程之间通信
import os, multiprocessing
from queue import Queue


def producer(x):
    for i in range(10):
        print("生产了++++++++pid{} {}".format(os.getpid(), i))
        x.put("pid{} {}".format(os.getpid(), i))


def consume(x):
    for i in range(10):
        print("消费了--------{}".format(x.get()))


if __name__ == "__main__":
    q = Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p1.start()

    c2 = multiprocessing.Process(target=consume, args=(q,))
    c2.start()
