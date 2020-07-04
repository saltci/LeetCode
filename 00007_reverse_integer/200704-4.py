#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # int32范围:  [−2**31,  2**31 − 1]（-2147483648～2147483647）
        boundry = (1<<31) -1 if x >0 else 1<<31        
        y,res = abs(x),0

        while y != 0:
            res = res*10+y%10
            if res > boundry:
                return 0
            y //= 10
        
        return res if x>0 else -res
        
# @lc code=end

# 1032/1032 cases passed (32 ms)
# Your runtime beats 98.68 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.7 MB)