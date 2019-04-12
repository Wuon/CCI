class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        rMax = []
        cMax = []
        total = 0
        for row in grid:
            m = 0
            for num in row:
                if num > m:
                    m = num
            rMax.append(m)
        for i in range(len(grid[0])):
            m = 0
            for j in range(len(grid)):
                if grid[j][i] > m:
                    m = grid[j][i]
            cMax.append(m)
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                total += (rMax[j] if rMax[j] < cMax[i] else cMax[i]) - grid[j][i]
        return total
