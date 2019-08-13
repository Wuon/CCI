#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += triangle[i - 1][j] if triangle[i-1][j] < triangle[i - 1][j - 1] else triangle[i - 1][j - 1]
            triangle[i][len(triangle[i]) - 1] += triangle[i-1][len(triangle[i - 1]) - 1]
        return min(triangle[len(triangle) - 1])
# @lc code=end
