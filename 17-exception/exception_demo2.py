try:
    file = open("ddd.txt", "r")
    print(file.read())
    file.close()
# except Exception as e:
#     print(e)
# except:
#     print("出错了")

except FileNotFoundError as e: # 处理指定类型的异常
    print(e)