class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        start = head
        end = head
        size = 0
        while end.next is not None:
            end = end.next
            size += 1
        i = 0
        while i < size:
            if (i+1) % 2 == 1:
                end.next = start.next
                end = end.next
                start.next = start.next.next
                i += 1
            start = start.next
            i += 1
        end.next = None
        return head
