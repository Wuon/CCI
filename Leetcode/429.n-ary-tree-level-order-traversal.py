#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self._o = []
        self.traverse(root)
        return self._o

    def traverse(self, root, level = 0):
        if not root:
            return
        if len(self._o) - 1 < level:
            self._o.append([])
        self._o[level].append(root.val)
        for child in root.children:
            self.traverse(child, level + 1)

# @lc code=end
