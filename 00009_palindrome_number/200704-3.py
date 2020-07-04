#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# @lc code=end

# 11509/11509 cases passed (88 ms)
# Your runtime beats 60.77 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (13.7 MB)

