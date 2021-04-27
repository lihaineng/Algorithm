"""
题目
给定一个整数的数组nums，返回相加为target的两个数字的索引值。

假设每次输入都只有一个答案，并且不会使用同一个元素两次。

举例：

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :param nums: 输入的列表
        :param target: 要检测的目标和
        :return:
        """
        if len(nums) < 2:
            return []
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

if __name__ == '__main__':
    s = Solution()
    a = s.twoSum([2, 11, 15, 7], 9)
    print(a)