class Solution(object):
    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, root, min=None, max=None):
        if root is None:
            return True
        if min is not None and min.val >= root.val:
            return False
        if max is not None and max.val <= root.val:
            return False
        return self.helper(root.left, min, root) and self.helper(root.right, root, max)
