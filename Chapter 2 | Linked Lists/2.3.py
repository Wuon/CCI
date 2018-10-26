# ATTEMPT ONE
#
# Time Complexity: O(1)
#
# This question can be interpreted as removing,
# any node in a linked list. Since the reference
# of the node is given, all that needs to happen
# is reassign the current node's data to the next
# and have the current node's next be the next next
# node. This will remove the reference of the next node.


def delete_middle_node(n):
    if n.get_next().get_next() is None:
        return False
    n.data = n.get_next().data
    n.set_next(n.get_next().get_next())
    return True
