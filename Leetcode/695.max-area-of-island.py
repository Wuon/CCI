#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        state = [[False] * len(grid[0]) for _ in range(len(grid))]
        area = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1 and state[row][column] == False:
                    stack = [(row, column)]
                    currentArea = 0
                    while stack:
                        cur = stack.pop()
                        if 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]):
                            if grid[cur[0]][cur[1]] == 1 and state[cur[0]][cur[1]] == False:
                                currentArea += 1
                                state[cur[0]][cur[1]] = True
                                stack.append((cur[0] + 1, cur[1]))
                                stack.append((cur[0] - 1, cur[1]))
                                stack.append((cur[0], cur[1] + 1))
                                stack.append((cur[0], cur[1] - 1))
                    if currentArea > area:
                        area = currentArea
        return area

# @lc code=end
