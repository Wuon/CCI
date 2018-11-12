# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# To complete the question, there must be one
# full iteration through the linked list.
# When the current node is less than p, reassign
# the node back to the beginning. When the current
# node is greater than p, reassign the node to the end.
# At the end of the iteration, the tail will point to
# the end of the linked list but will point to the head
# making it a circular linked list. We then removed the
# assigned reference to null to complete the problem.
# Please view the attached pdf to see the work.


def partition(n, p):
    head = n
    tail = n
    while n is not None:
        s = n.get_next()
        if n.get_data() < p:
            n.set_next(head)
            head = n
        else:
            tail.set_next(n)
            tail = n
        n = s
    tail.set_next(None)
    return head
