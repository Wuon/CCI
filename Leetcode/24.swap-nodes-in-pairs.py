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
        if not head:
            return None
        if head.next is None:
            return head
        count = 1
        dummy = ListNode(None)
        dummy.next = head
        temp = dummy
        while head:
            if count == 2:
                count = 0
                dummy.next.next = head.next
                head.next = dummy.next
                dummy.next = head
                dummy = dummy.next.next
                head = head.next
            count += 1
            head = head.next
        return temp.next
# @lc code=end
