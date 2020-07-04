#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        int32_range = {
            "min":-2 ** 31,
            "max":2 ** 31 -1,
        }

        reverse_num = 0

        if x < int32_range["min"] or x > int32_range["max"]:
            return reverse_num

        if x > 0:
            to_str = str(x)
            reverse_num = int(to_str[::-1])

        elif x < 0:
            to_str = str(abs(x))
            reverse_num = int(to_str[::-1]) * -1
        
        else:
            reverse_num = 0
        
        if reverse_num < int32_range["min"] or reverse_num > int32_range["max"]:
            return 0
        
        return reverse_num

# @lc code=end

# 1032/1032 cases passed (48 ms)
# Your runtime beats 44.87 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.7 MB)