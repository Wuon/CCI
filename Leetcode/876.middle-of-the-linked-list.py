#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = b = head
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
        if b.next:
            a = a.next
        return a
# @lc code=end
