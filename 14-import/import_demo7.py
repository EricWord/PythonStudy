import calendar  # 日历模块

# 设置每一周的第一天是周几
calendar.setfirstweekday(calendar.SUNDAY)
# 打印2021年的日历
print(calendar.calendar(2021))
# 判断是否是闰年
print(calendar.isleap(2021))
# 判断两个间隔年份之间由多少个闰年
print(calendar.leapdays(1996, 2010))
# 打印某一年某个月份的日志
print(calendar.month(2021, 3))
