#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            pre = pre.next
        cur= pre.next
        node = None
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        pre.next.next = cur
        pre.next = node
        return dummy.next

# @lc code=end
