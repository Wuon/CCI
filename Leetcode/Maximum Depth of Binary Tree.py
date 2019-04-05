class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        return (right if right > left else left) + 1
