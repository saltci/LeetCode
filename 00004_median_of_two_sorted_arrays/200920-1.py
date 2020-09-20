#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数 => 暴力解法
# 思路:
# 1. 合并两个列表
# 2. 对合并之后的列表进行排序
# 3. 判断列表的长度是奇数还是偶数
# 4. 根据列表的长度返回中位数
# 提交记录
# 2091/2091 cases passed (52 ms)
# Your runtime beats 84.34 % of python3 submissions
# Your memory usage beats 43.61 % of python3 submissions (13.5 MB)
# 题解: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/di-k-xiao-shu-jie-fa-ni-zhen-de-dong-ma-by-geek-8m/

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list.sort()

        list_length = len(merge_list)
        if list_length % 2 == 0:
            return (merge_list[int(list_length/2)] + merge_list[int(list_length/2 -1)]) / 2
        else:
            return merge_list[list_length//2]

# @lc code=end