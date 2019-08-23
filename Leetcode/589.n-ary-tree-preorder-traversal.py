#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self._o = []
        self.traverse(root)
        return self._o

    def traverse(self, root):
        if not root:
            return
        self._o.append(root.val)
        for child in root.children:
            self.traverse(child)
# @lc code=end
