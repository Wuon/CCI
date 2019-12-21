#
# @lc app=leetcode id=863 lang=python
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        d = {}
        q = []
        if not root:
            return q
        if K == 0:
            return [target.val]
        self.traverse(root, d)
        q.append(target)
        depth = 0
        s = set()
        while q:
            newq = []
            for node in q:
                if node in d:
                    if node not in s:
                        newq.append(d[node])
                        s.add(node)
                if node.right:
                    if node.right not in s:
                        newq.append(node.right)
                        s.add(node.right)
                if node.left:
                    if node.left not in s:
                        newq.append(node.left)
                        s.add(node.left)
            depth += 1
            if depth > K:
                return []
            q = newq
            if depth == K:
                break
        output = []
        for node in q:
            output.append(node.val)
        return output

    def traverse(self, root, d):
        if root:
            if root.left:
                d[root.left] = root
            if root.right:
                d[root.right] = root
            self.traverse(root.right, d)
            self.traverse(root.left, d)
# @lc code=end
