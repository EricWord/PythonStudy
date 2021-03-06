import threading

# 多线程安全问题
import time

ticket = 20
# 创建一把锁
l = threading.Lock


def sell_ticket():
    global ticket
    while True:
        # 加同步锁
        # l.
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            l.release()
            print("{}卖出一张票，还剩{}张".format(threading.current_thread().name, ticket))
        else:
            l.release()
            print("票卖完了")
            break


t1 = threading.Thread(target=sell_ticket, name="线程1")
t2 = threading.Thread(target=sell_ticket, name="线程2")

t1.start()
t2.start()
