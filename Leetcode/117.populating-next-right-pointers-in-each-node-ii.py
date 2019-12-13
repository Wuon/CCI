#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q = deque()
        root.next = None
        q.append(root)
        while q:
            newQ = deque()
            while q:
                cur = q.popleft()
                if cur.left:
                    newQ.append(cur.left)
                if cur.right:
                    newQ.append(cur.right)
            prev = None
            for node in newQ:
                if prev is None:
                    prev = node
                else:
                    prev.next = node
                    prev = node
            if prev:
                prev.next = None
            q = newQ
        return root
# @lc code=end
