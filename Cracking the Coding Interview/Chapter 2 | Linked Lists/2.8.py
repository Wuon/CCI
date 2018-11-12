# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# First we need to check if a loop occurs in the linked list. This
# is done by having a fast and slow runner. Because one moves twice
# as the other, the faster one will overlap the smaller runner at
# the second iteration. When they do overlap its exactly doubled
# minus the starting length of the loop. Using this information
# we can then traverse from the point in the loop and at the
# beginning of the linked list. If they match, then the linked list
# has a loop.

def loop_detection(l):

    f = l.head
    s = l.head
    n = l.head

    while f is not None and f.get_next() is not None:
        f = f.get_next().get_next()
        s = s.get_next()
        if f is s:
            break

    if f is None or f.get_next() is None:
        return None

    while f is not n:
        f = f.get_next()
        n = n.get_next()

    return n

