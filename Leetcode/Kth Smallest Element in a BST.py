# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        store = []
        self.helper(root, store)
        return store[k-1]

    def helper(self, root, store):
        if root:
            self.helper(root.left, store)
            store.append(root.val)
            self.helper(root.right, store)
