#
# @lc app=leetcode id=590 lang=python
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root):
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
        for child in root.children:
            self.traverse(child)
        self._o.append(root.val)
# @lc code=end
