#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # int32范围:  [−2**31,  2**31 − 1]（-2147483648～2147483647）
        if -10 < x < 10:
            return x

        rev = 0
        x_sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        
        rev *= x_sign

        if rev > 2147483647 or rev < -2147483648:
            return 0
        
        return rev

# @lc code=end

# 1032/1032 cases passed (48 ms)
# Your runtime beats 44.87 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.6 MB)