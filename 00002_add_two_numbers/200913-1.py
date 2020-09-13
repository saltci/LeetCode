#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_number(self,input_number):
        num = str(input_number.val)
        _next = input_number.next

        if _next:
            while _next:
                temp = _next
                _num = str(temp.val)
                num += _num
                _next = _next.next
        
        return int(num[::-1])

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_1 = self.get_number(l1)
        num_2 = self.get_number(l2)

        sum_result = num_1 + num_2
        sum_str = str(sum_result)[::-1]
        print(sum_str)

        new_list_node = ListNode(int(sum_str[0]))
        temp_node = new_list_node

        for i in range(len(sum_str)):
            if i + 1 < len(sum_str):
                next_list_node = ListNode(int(sum_str[i+1]))
                temp_node.next = next_list_node
                temp_node = next_list_node

        return new_list_node
# @lc code=end

