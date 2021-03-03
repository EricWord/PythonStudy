words = ["hello", "good", "today", "hadoop"]
nums = (9, 4, 3, 1, 7, 6)
print(nums[3])
# nums[3] = 49 元组不可变，这里会报错
print(nums.index(7))
print(nums.count(9))
# 特殊情况：如何表示只有一个元素的元组？
ages = (18)
print(type(ages))  # <class 'int'>
# 如果元组里只有一个元组，需要在元素后面添加一个逗号
ages2 = (18,)
print(type(ages2))  # <class 'tuple'>

# 列表转元组
print(tuple(words))

# 元组转列表
print(list(nums))