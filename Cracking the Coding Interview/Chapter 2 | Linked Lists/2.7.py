# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# If an intersection every occures then the last node must have the
# same reference. Therefore the first thing we check for is the last
# node. By doing this, we also get the size of both linked lists.
# After, if such intersection occurs before hand, we can take the
# difference between the lists. Go forward on the bigger one just
# it matches up with the shorter one and iterate through to see
# if a match in reference occurs.


def intersection(l1, l2):

    h1 = l1.head
    h2 = l2.head
    c1 = 0
    c2 = 0

    while h1.get_next() is not None or h2.get_next() is not None:
        if h1.get_next() is not None:
            h1 = h1.get_next()
            c1 += 1
        if h2.get_next() is not None:
            h2 = h2.get_next()
            c2 += 1

    if h1 is h2:
        return h1

    b = l1.head if c1 > c2 else l2.head
    s = l1.head if c1 < c2 else l2.head

    for i in range(0, abs(c1-c2)):
        b = b.get_next()

    while b is not None:
        if b is s:
            return b
        b = b.get_next()
        s = s.get_next()

    return None
