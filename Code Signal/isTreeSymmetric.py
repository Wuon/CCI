#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isTreeSymmetric(t):
    q = []
    q.append(t)
    q.append(t)
    while q:
        curNode1 = q.pop()
        curNode2 = q.pop()
        if (curNode1 == None and curNode2 == None):
            continue
        if (curNode1 == None or curNode2 == None):
            return False
        if curNode1.value != curNode2.value:
            return False
        q.append(curNode1.left)
        q.append(curNode2.right)
        q.append(curNode1.right)
        q.append(curNode2.left)
    return True
