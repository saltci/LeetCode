#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}

        for i in range(len(nums)):
            if nums[i] not in temp_dict:
                temp_dict[target - nums[i]] = i
            else:
                return [temp_dict[nums[i]],i]
# @lc code=end

# 29/29 cases passed (60 ms)
# Your runtime beats 81.71 % of python3 submissions
# Your memory usage beats 5.48 % of python3 submissions (14.9 MB)