# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def reverseLinkedList(l):
    prev = None
    current = l
    while current: 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
    return prev 


def isListPalindrome(l):
    length = 0
    head = l

    while head:
        length += 1
        head = head.next

    mid = length // 2
    head = l

    for i in range(mid):
        head = head.next
    
    head = reverseLinkedList(head)

    for i in range(mid):
        if l.value != head.value:
            return False
        l = l.next
        head = head.next

    return True
