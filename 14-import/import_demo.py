# 1. 使用import 模块名直接导入一个模块
import time

# 导入这个模块以后，就可以使用这个模块里的方法和变量
print(time.time())
# 2.from 模块名 import 函数名,导入一个模块里的方法或者变量
from random import randint

# 生成[0,2]的随机数
randint(0, 2)
# 3.from 模块名 import * 导入这个模块里的所有方法和变量
from math import *

print(pi)
# 4.导入一个模块，并起别名
import datetime as dt

print(dt.MAXYEAR)

# 5.from 模块名 import 函数名 as 别名
from copy import deepcopy as dp

dp(["hello", [1, 2, 3], "good"])
