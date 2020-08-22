from collections import deque

testCase1 = [[1,1,1,1,1],
    [1,0,0,1,1],
    [1,0,0,1,1],
    [1,1,1,1,1]]

testCase2 = [[1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1]]

testCase3 = [[1,1,1,1,1],
    [1,0,0,1,1],
    [1,0,0,1,1],
    [1,1,1,1,0]]

def findCoordinates(grid):
    output = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0 and (i,j) not in visited:
                start = [i,j]
                queue = deque([(i,j)])
                end = []
                while queue:
                    curI, curJ = queue.popleft()
                    if curI < len(grid) and curJ < len(grid[0]) and (curI,curJ) not in visited and grid[curI][curJ] == 0:
                        visited.add((curI,curJ))
                        queue.append((curI+1, curJ))
                        queue.append((curI, curJ+1))
                        end = [curI, curJ]
                output.append([start, end])
    return output

print(findCoordinates(testCase1))
print(findCoordinates(testCase2))
print(findCoordinates(testCase3))
