class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        length = 0
        a = head
        while a:
            a = a.next
            length += 1
        a = head
        for i in range(0, length // 2):
            a = a.next
        a = self.reverseList(a)
        for i in range(0, length // 2):
            if a.val != head.val:
                return False
            a = a.next
            head = head.next
        return True

    def reverseList(self, head: 'ListNode') -> 'ListNode':
        return self.helper(None, head)

    def helper(self, prev, head):
        if head is None:
            return prev
        new = self.helper(head, head.next)
        head.next = prev
        return new
