class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if root:
            self.helper(root, val)
        else:
            root = TreeNode(val)
        return root

    def helper(self, root, val):
        if val > root.val:
            if root.right:
                self.helper(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                self.helper(root.left, val)
            else:
                root.left = TreeNode(val)
