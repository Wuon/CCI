#
# @lc app=leetcode id=1252 lang=python
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count = 0
        grid = [[0 for x in range(m)] for y in range(n)]
        for pair in indices:
            for i in range(m):
                grid[pair[0]][i] += 1
            for i in range(n):
                grid[i][pair[1]] += 1
        for i in range(m):
            for j in range(n):
                if grid[j][i] % 2 == 1:
                    count += 1
        return count
# @lc code=end
