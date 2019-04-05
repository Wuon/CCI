class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        return self.helper(None, head)

    def helper(self, prev, head):
        if head is None:
            return prev
        new = self.helper(head, head.next)
        head.next = prev
        return new
