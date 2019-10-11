#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        results = []
        if n == 0:
            return results
        stack.append(["(", 1, 0])
        while stack:
            cur = stack.pop()
            if len(cur[0]) == n * 2:
                results.append(cur[0])
            else:
                if cur[1] < n:
                    stack.append([cur[0] + "(", cur[1] + 1, cur[2]])
                if cur[2] < cur[1]:
                    stack.append([cur[0] + ")", cur[1], cur[2] + 1])
        return results
# @lc code=end
