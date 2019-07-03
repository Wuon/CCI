"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = {}
        self.traverse(root, d)
        for k in d:
            d[k].next = None
        return root

    def traverse(self, root, d, count = 0):
        if root:
            if count in d:
                d[count].next = root
            d[count] = root
            count += 1
            self.traverse(root.left, d, count)
            self.traverse(root.right, d, count)
