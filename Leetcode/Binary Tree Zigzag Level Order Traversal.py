# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        store = []
        self.helper(root, 0, store)
        for i in range(len(store)):
            if i % 2 == 0:
                store[i].reverse()
        return store

    def helper(self, root, depth, store):
        if root is None:
            return
        while len(store) <= depth:
            store.append([])
        self.helper(root.right, depth + 1, store)
        store[depth].append(root.val)
        self.helper(root.left, depth + 1, store)
