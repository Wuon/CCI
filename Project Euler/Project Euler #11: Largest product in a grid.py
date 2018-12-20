#!/bin/python3

import sys

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
maximum = 0
for y in range(20):
    for x in range(20):
        for direction in [[0, 1], [1, 0], [1, 1], [-1, 1]]:
            try:
                prod = grid[y][x] * grid[y + direction[0]][x + direction[1]] * grid[y + direction[0]*2][x + direction[1]*2] * grid[y + direction[0]*3][x + direction[1]*3]
                maximum = prod if prod > maximum else maximum
            except IndexError:
                pass
print(maximum)
