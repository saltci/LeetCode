#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: return result
            if i>0 and nums[i] == nums[i-1]: continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_result = nums[i] + nums[left] + nums[right]
                if sum_result == 0:
                    result.append([nums[i] ,nums[left] ,nums[right]])
                    while left<right and nums[left] == nums[left+1]: left+=1
                    while left<right and nums[right] == nums[right-1]: right-=1

                    left+=1
                    right-=1
                elif sum_result < 0:
                    left+=1
                elif sum_result > 0:
                    right-=1
        return result
# @lc code=end

