# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def removeKFromList(l, k):
    prevNode = ListNode(-1)
    prevNode.next = l
    head = prevNode
    while l:
        if l.value == k:
            prevNode.next = l.next
        else:
            prevNode = l
        l = l.next
    return head.next
