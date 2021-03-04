# sort方法中使用匿名函数
students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 21, "score": 97, "height": 185},
    {"name": "jack", "age": 22, "score": 100, "height": 175},
    {"name": "tony", "age": 23, "score": 90, "height": 176},
    {"name": "henry", "age": 20, "score": 95, "height": 172},
]


def cmp(ele):
    # print(ele)
    # 通过返回值告诉排序函数根据哪个字段进行排序
    return ele["height"]


# 需要传入key，指定比较规则
# students.sort(key=cmp)
# 上面的写法使用匿名函数的写法如下
students.sort(key=lambda ele: ele["height"])
print(students)  # TypeError: '<' not supported between instances of 'dict' and 'dict'
