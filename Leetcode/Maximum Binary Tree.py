# TODO optimize solution
import copy


class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if len(nums) == 0:
            return []
        node = TreeNode(nums[0])
        for i in range(1, len(nums)):
            self.helper(node, nums[i])
        return node

    def helper(self, node, num):
        if num < node.val:
            if node.right:
                self.helper(node.right, num)
            else:
                node.right = TreeNode(num)
        else:
            temp = copy.copy(node)
            node.right = None
            node.val = num
            node.left = temp
