score = float(input("请输入您的成绩："))
if 60 > score >= 0:
    print("垃圾")
elif score < 80:
    print("一般")
elif score < 90:
    print("良好")
else:
    print("优秀！")
