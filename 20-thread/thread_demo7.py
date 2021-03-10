import multiprocessing, queue

q2 = queue.Queue()  # 线程间通信
# 创建队列时，可以指定最大长度，默认值是0，表示不限长度
q1 = multiprocessing.Queue(5)  # 进程间通信

q1.put("1")
q1.put("1")
q1.put("1")
q1.put("1")
q1.put("1")
# q1.put("2") # 放不进去，可以发现队列里可以放入重复的元素
# block=True表示是阻塞的，即如果队列已经满了，就等待
# timeout超时，等待多久以后程序会出错，单位是秒
# q1.put("2", block=True, timeout=1)
# q1.put_nowait("3")  # 等价于q1.put("3",block=False)


print(q1.get())
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.get())
# q1.get(block=True, timeout=1)
q1.get_nowait()
