import copy

# 浅拷贝
nums = [1, 2, 3, 4, 5]
nums1 = nums  # 这个既不是深拷贝也不是浅拷贝
nums2 = nums.copy()  # 浅拷贝 ，两个内容一模一样，但是不是同一个对象
nums3 = copy.copy(nums)  # 和 nums.copy()功能一样，都是浅拷贝

# 深拷贝只能使用copy模块来实现
words = ["hello", "good", [100, 200, 300], "yes", "hi", "ok"]
# words1是word的浅拷贝
words1 = words.copy()
# words[0] = "你好"
# words[2][0] = 1
# print(words1)
# 深拷贝
words2 = copy.deepcopy(words)
words[2][0] = 1
print(words2)