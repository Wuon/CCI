#
# @lc app=leetcode id=1254 lang=python
#
# [1254] Number of Closed Islands
#

# @lc code=start

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        stack = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == False and grid[row][col] == 0:
                    stack.append((row, col))
                    isIsland = True
                    while stack:
                        pair = stack.pop()
                        if(0 <= pair[0] < len(grid) and 0 <= pair[1] < len(grid[0])):
                            if visited[pair[0]][pair[1]] == False and grid[pair[0]][pair[1]] == 0:
                                visited[pair[0]][pair[1]] = True
                                stack.append((pair[0], pair[1]+1))
                                stack.append((pair[0]+1, pair[1]))
                                stack.append((pair[0], pair[1]-1))
                                stack.append((pair[0]-1, pair[1]))
                        else:
                            isIsland = False
                    if isIsland:
                        count += 1
        return count
# @lc code=end
