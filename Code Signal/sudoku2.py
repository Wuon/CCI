def isRowLegal(grid):
    for row in grid:
        s = set()
        for number in row:
            if number == '.':
                continue
            if number in s:
                return False
            else:
                s.add(number)
    return True
    
def isColLegal(grid):
    for i in range(len(grid)):
        s = set()
        for j in range(len(grid)):
            number = grid[j][i]
            if number == '.':
                continue
            if number in s:
                return False
            else:
                s.add(number)
    return True
    
def isSquareLegal(grid):
    for i in range(len(grid)):
        s = set()
        for j in range(len(grid)):
            row = (j // 3) + (i // 3) * 3
            col = j % 3 + (i % 3) * 3
            number = grid[row][col]
            if number == '.':
                continue
            if number in s:
                return False
            else:
                s.add(number)
    return True

def sudoku2(grid):
    return isRowLegal(grid) and isColLegal(grid) and isSquareLegal(grid)
