# 冒泡排序
nums = [6, 5, 3, 1, 8, 7, 2, 4]
n = 0
while n < len(nums) - 1:
    if nums[n] > nums[n + 1]:
        nums[n], nums[n + 1] = nums[n + 1], nums[n]
    n += 1

print(nums)
