from SinglyLinkedList import LinkedList

# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# For this question, if the size of the singly linked
# list is known, iterate until kth element. If not, recursively
# find the size (or iteratively) then compute for kth to last.


def return_kth_to_last(l, k):
    for i in range(0, l.size()-k-1):
        l.head = l.head.get_next()
    return l


def return_kth_to_last2(l, k):
    for i in range(0, recursive(l.head, k)-k-1):
        l.head = l.head.get_next()
    return l


def recursive(h, k):
    if h is None:
        return 0
    return recursive(h.get_next(), k) + 1


s = LinkedList()
s.insert("a")
s.insert("b")
s.insert("c")

return_kth_to_last2(s, 1).print()

print(recursive(s.head, 1))
