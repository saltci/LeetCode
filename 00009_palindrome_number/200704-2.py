#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数直接返回False
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        
        # reverse整数
        reverse_number = 0

        while x > reverse_number:
            reverse_number = reverse_number * 10 + x % 10
            x //= 10
        
        return x == reverse_number or x == reverse_number // 10


# @lc code=end

# 11509/11509 cases passed (96 ms)
# Your runtime beats 40.29 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.7 MB)
