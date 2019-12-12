#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = prev = ListNode(None)
        new.next = head
        first = None
        while head:
            if first is None:
                first = head
                head = first.next
            else:
                first.next = head.next
                head.next = first
                prev.next = head
                prev = first
                first = None
                head = prev.next
        return new.next
# @lc code=end
