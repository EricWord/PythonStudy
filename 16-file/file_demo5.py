# csv文件的读写
import csv

# 打开一个文件
file = open("demo2.csv", "w")
writer = csv.writer(file)
# writerow 每次写一行
# writer.writerow(["name", "age", "score", "city"])
# writer.writerow(["张三", "19", "90", "深圳"])
# writer.writerow(["李四", "19", "90", "纽约"])


# 也可以一次写多行
# writer.writerows(
#     [["name", "age", "score", "city"],
#      ["张三", "19", "90", "深圳"],
#      ["李四", "19", "90", "纽约"]]
# )


# csv文件的读取
file = open("demo.csv", "r", encoding="utf8", newline="")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()
