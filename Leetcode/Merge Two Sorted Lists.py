class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if None in (l1, l2):
            return l1 or l2
        dummy = l1
        head = l2
        l1 = l1.next
        if dummy.val <= l2.val:
            dummy.next = l2
            head = dummy
            dummy = l1
            l2 = head
        else:
            l1 = dummy
        while l1 and l2:
            l1 = l1.next
            if l2.val <= dummy.val <= (l2.next.val if l2.next is not None else l2.val) :
                dummy.next = l2.next
                l2.next = dummy
                dummy = l1
            else:
                l1 = dummy
            if l2.next is None:
                l2.next = dummy
                break
            else:
                l2 = l2.next
        if l2 is None:
            l2.next = dummy
        return head
