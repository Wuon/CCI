# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        a = head
        b = head
        for i in range(0, n + 1):
            if b is None:
                return a.next
            b = b.next
        while b is not None:
            b = b.next
            a = a.next
        a.next = a.next.next
        return head
