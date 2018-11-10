# ATTEMPT ONE
#
# Time Complexity: O(n log(n))
#
# To generate a tree of minimal height, its best to start at the middle
# of the given array. That way we will have an even amount of nodes on the right and left
# This is especially true given that the array is sorted in an increasing order.
# We then just insert the node traversing the tree through the array. This problem
# can also be solved recursively for a faster runtime. This will be revisited at a later time.
#
# TODO - recursive solution


def minimal_tree(l):
    start = Node(l[len(l) // 2])
    for n in range(1, len(l) // 2 + len(l) % 2):
        start.insert(l[len(l) // 2 - n])
        start.insert(l[len(l) // 2 + n])
    if len(l) % 2 == 0:
        start.insert(l[0])
    return start


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
