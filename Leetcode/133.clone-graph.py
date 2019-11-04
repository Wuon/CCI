#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        c = Node(node.val, [])
        stack = [node]
        visited = {}
        visited[node.val] = c
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[cur.val].neighbors.append(visited[neighbor.val])
        return c
# @lc code=end
