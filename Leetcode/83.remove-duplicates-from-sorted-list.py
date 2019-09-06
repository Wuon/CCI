#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        temp = head
        s = set()
        prev = ListNode(None)
        while temp.next:
            if temp.val not in s:
                s.add(temp.val)
                prev = temp
            else:
                prev.next = temp.next
            temp = temp.next
        if temp.val in s:
            prev.next = None
        return head
# @lc code=end
