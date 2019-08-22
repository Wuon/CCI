#
# @lc app=leetcode id=993 lang=python
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self._d = {}
        self.search(root)
        if x in self._d and y in self._d:
            return self._d[x][0] == self._d[y][0] and self._d[x][1] != self._d[y][1]
        return False

    def search(self, root, level = 0, parent = None):
        if not root:
            return
        self._d[root.val] = [level, parent]
        self.search(root.left, level + 1, root.val)
        self.search(root.right, level + 1, root.val)
# @lc code=end
