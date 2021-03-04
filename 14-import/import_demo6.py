import datetime as dt

# 获取当前日期
print(dt.datetime.now())
# 创建一个日期
print(dt.date(2021, 1, 1))
# 创建一个时间
print(dt.time(18, 23, 45))
# 计算3天以后的时间
print(dt.datetime.now() + dt.timedelta(3))
