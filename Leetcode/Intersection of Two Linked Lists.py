class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sizeA = 0
        sizeB = 0
        refA = headA
        refB= headB
        while refA is not None:
            refA = refA.next
            sizeA += 1
        while refB is not None:
            refB = refB.next
            sizeB += 1
        refA = headA if sizeA >= sizeB else headB
        refB = headB if sizeB <= sizeA else headA
        for i in range(0, abs(sizeA-sizeB)):
            refA = refA.next
        while refA is not None:
            if refA == refB:
                return refA
            refA = refA.next
            refB = refB.next
        return None
