#
# @lc app=leetcode id=1302 lang=python
#
# [1302] Deepest Leaves Sum
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        output = []
        q = [root]
        while q:
            nq = []
            cur = 0
            for node in q:
                cur += node.val
                if node.right:
                    nq.append(node.right)
                if node.left:
                    nq.append(node.left)
            output.append(cur)
            q = nq
        return output[-1]

# @lc code=end
