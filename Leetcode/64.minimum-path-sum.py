#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                a, b = -1, -1
                if 0 <= i - 1:
                    a = grid[i-1][j]
                if 0 <= j - 1:
                    b = grid[i][j-1]
                if a == -1 and b == -1:
                    grid[i][j] += 0
                elif a == -1:
                    grid[i][j] += b
                elif b == -1:
                    grid[i][j] += a
                else:
                    grid[i][j] += a if a < b else b
        return grid[len(grid) - 1][len(grid[len(grid) - 1]) - 1]

# @lc code=end
