class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        l3 = spectator = ListNode(0)
        carry = 0
        while l1 is not None and l2 is not None:
            l3.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1 is not None:
            l3.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            l3 = l3.next
        while l2 is not None:
            l3.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            l3 = l3.next
        if carry != 0:
            l3.next = ListNode(carry)
        return spectator.next
