# 调用列表的sort方法可以直接对列表进行排序
nums = [6, 5, 3, 1, 8, 7, 2, 4]
# 升序排序，直接对原有的列表进行排序
nums.sort()
# 倒序排序
nums.sort(reverse=True)
print(nums)

# 使用内置函数sorted()进行排序
newNums = sorted(nums,reverse=True)
print(newNums)
