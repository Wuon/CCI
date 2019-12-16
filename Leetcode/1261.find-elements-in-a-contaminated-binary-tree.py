#
# @lc app=leetcode id=1261 lang=python
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    s = set()

    def __init__(self, root: TreeNode):
        self.s = set()
        root.val = 0
        self.rebuild(root)


    def find(self, target: int) -> bool:
        return target in self.s

    def rebuild(self, root, val = 0):
        if not root:
            return
        root.val = val
        self.s.add(val)
        self.rebuild(root.right, root.val * 2 + 2)
        self.rebuild(root.left, root.val * 2 + 1)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# @lc code=end
