#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def hasPathWithGivenSum(t, s):
    q = []
    if t is None:
        return False
    q.append((t, t.value))
    while len(q) != 0:
        node, value = q.pop()
        if node.right:
            res = value + node.right.value
            q.append((node.right, res))
        if node.left:
            res = value + node.left.value
            if res == s:
                return True
            q.append((node.left, res))
        if node.right is None and node.left is None:
            if value == s:
                return True
    return False
