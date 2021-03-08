# 使用迭代器实现斐波那契数列
import time


class Fib:
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < self.n:
            x = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            # time.sleep(1)
            return x
        else:
            raise StopIteration


f = Fib(12)
for i in f:
    print(i)
