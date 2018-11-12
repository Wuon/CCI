# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# This should perform much like adding numbers on paper.
# If adding two numbers give more than 9, then we have
# a carry to the next place value. We iterate through
# both linked lists exactly once.


from SinglyLinkedList import LinkedList


def sum_lists(n1, n2):
    c = 0
    n3 = LinkedList()
    while n1 is not None:
        n3.insert(n1.get_data() + n2.get_data()-10 + c
                  if n1.get_data() + n2.get_data() + c > 9 else n1.get_data() + n2.get_data() + c)
        c = 1 if n1.get_data() + n2.get_data() + c > 9 else 0
        n1 = n1.get_next()
        n2 = n2.get_next()
    return n3
