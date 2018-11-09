# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# For this problem, each node should have three states. I represented this
# by having null, true and false. This should be enough information to know
# if a node has not been visited, has been visited, and is going to be visited.
# This iterative approach cycles through at worse case at least once to every node.
# Beginning with the starting node, we check for any adjacent nodes and check to see
# if it hasn't been visited yet. We then add it to the queue to be traversed at a later time.
# Eventually, if a path has been established, will return true when one of the adjacent sides
# is the end node.


def route_between_nodes(n1, n2):
    paths = Queue()
    paths.enqueue(n1)
    n1.state = False
    while not paths.is_empty():
        path = paths.dequeue()
        if path is not None:
            for node in path.get_adjacent():
                if node.state is None:
                    if node == n2:
                        return True
                    node.state = False
                    paths.enqueue(node)
        path.state = True
    return False


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.state = None
        self.adjacent = []

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def add_adjacent(self, node):
        self.adjacent.append(node)

    def get_adjacent(self):
        return self.adjacent


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0;

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.size += 1
        self.items.insert(0,item)

    def dequeue(self):
        self.size -= 1
        return self.items.pop()

    def size(self):
        return self.size

    def peek(self):
        return self.items[self.size - 1]
