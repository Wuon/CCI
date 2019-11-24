#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pointerA = pointerB = head
        isCycle = False
        while pointerB.next and pointerB.next.next:
            pointerA = pointerA.next
            pointerB = pointerB.next.next
            if pointerA == pointerB:
                isCycle = True
                break
        if isCycle:
            pointerA = head
            while pointerA != pointerB:
                pointerA = pointerA.next
                pointerB = pointerB.next
            return pointerA
        return None
# @lc code=end
