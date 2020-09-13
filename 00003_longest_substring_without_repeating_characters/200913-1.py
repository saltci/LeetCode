#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def get_str(self,input_str):
        temp = set()
        output_str = ''

        for i in input_str:
            if i not in temp:
                output_str += i
                temp.add(i)
            else:
                break

        return len(output_str)

    def lengthOfLongestSubstring(self, s: str) -> int:
        str_length = len(s)
        max_length = 0

        for i in range(str_length):
            count = self.get_str(s[i:str_length])

            if count > max_length:
                max_length = count
        
        return max_length
# @lc code=end

