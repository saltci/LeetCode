#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x

        to_str = str(x)

        if to_str[0] != "-":
            x = int(to_str[::-1])
        else:
            x = int(to_str[:0:-1]) * -1
        
        return x if -2147483648 < x < 2147483647 else 0

# @lc code=end

# 1032/1032 cases passed (44 ms)
# Your runtime beats 67.71 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.8 MB)