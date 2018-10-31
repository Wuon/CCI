# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# A little tricky, but basically the logic is as follows:
# If the linked list is of size 1 then it must be a a palindrome.
# We instantiate two new pointers f and b. One moves twice as fast
# as the other. This is important because in a palindrome, it must be
# mirrored. This is where the two steps one step come to play. Now one reference
# is at the end and the other is in the middle. We then reverse the middle to the end.
# Now we have a pointer in the middle and a pointer in the beginning. We compare from
# beginning to middle and middle to end. They should be the same. If not then its not
# a palindrome.


def palindrome(l):
    if l.head.get_next() is None:
        return True
    f = b = l.head
    while f.get_next() is None or f.get_next().get_next() is None:
        f = f.get_next().get_next()
        b = b.get_next()
    reverse(l, b.get_next())
    while f is not None:
        if f.get_data() != l.head.get_data():
            return False
        f = f.get_next()
        l.head = l.head.get_next()
    return True


def reverse(l, n):
    if n.get_next() is None:
        l.head = n
        return
    reverse(l, n.get_next())
    t = n.get_next()
    t.set_next(n)
    n.set_next(None)

