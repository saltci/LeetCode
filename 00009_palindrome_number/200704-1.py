#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数直接返回False
        if x < 0:
            return False
        
        # reverse整数
        temp,res = x, 0

        while temp != 0:
            res = res * 10 + temp % 10
            temp //= 10
        
        if res == x:
            return True
        else:
            return False


# @lc code=end

# 11509/11509 cases passed (108 ms)
# Your runtime beats 21.44 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.7 MB)