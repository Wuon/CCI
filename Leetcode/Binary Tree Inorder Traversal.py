class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        store = []
        self.helper(root, store)
        return store

    def helper(self, root, store):
        if not root:
            return
        self.helper(root.left, store)
        store.append(root.val)
        self.helper(root.right, store)
