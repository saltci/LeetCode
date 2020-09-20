#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串

# 103/103 cases passed (6816 ms)
# Your runtime beats 7.24 % of python3 submissions
# Your memory usage beats 87.56 % of python3 submissions (13.3 MB)

# @lc code=start

# 103/103 cases passed (64 ms)
# Your runtime beats 99.25 % of python3 submissions
# Your memory usage beats 74.07 % of python3 submissions (13.4 MB)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0: return ""
        if length == 1 or s == s[::-1]: return s

        start,max_len = 0,1
        for i in range(1, length):
            even = s[i - max_len: i + 1]
            odd = s[i - max_len - 1: i + 1]

            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
                continue
            
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
        
        return s[start: start + max_len]

# @lc code=end