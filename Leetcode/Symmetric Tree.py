class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        return self.helper(root.right, root.left)

    def helper(self, right, left):
        if not right and not left:
            return True
        if right and left:
            if right.val == left.val:
                r = self.helper(right.right, left.left)
                l = self.helper(left.right, right.left)
                return r and l
        return False
