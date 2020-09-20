#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
# 方法一: 反向暴力解法
# 1.设置变量max_palindromic = ''
# 2.双层循环遍历字符串,每次分别取字符串的切片[i:j],并判断是否为回文串,如果是回文串,与max_palindromic做比较,如果长度大于max_palindromic则把长度大的回文串赋值给max_palindromic

# 103/103 cases passed (4356 ms)
# Your runtime beats 46.35 % of python3 submissions
# Your memory usage beats 59.2 % of python3 submissions (13.4 MB)

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        length = len(s)

        for i in range(length, -1, -1):
            for j in range(0,length - i + 1):
                sub_string = s[j:i + j]
                if sub_string == sub_string[::-1]:
                    return sub_string


# @lc code=end