class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        island = 0
        if grid:
            visited = [x[:] for x in [[False] * len(grid[0])] * len(grid)]
            queue = []
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if visited[row][col] == False and grid[row][col] == "1":
                        queue.append((row, col))
                        while queue:
                            pair = queue.pop()
                            if(0 <= pair[0] < len(grid) and 0 <= pair[1] < len(grid[0])):
                                if visited[pair[0]][pair[1]] == False and grid[pair[0]][pair[1]] == "1":
                                    visited[pair[0]][pair[1]] = True
                                    queue.append((pair[0], pair[1]+1))
                                    queue.append((pair[0]+1, pair[1]))
                                    queue.append((pair[0], pair[1]-1))
                                    queue.append((pair[0]-1, pair[1]))
                        island += 1
        return island
