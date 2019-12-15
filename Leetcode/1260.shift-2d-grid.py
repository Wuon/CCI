#
# @lc app=leetcode id=1260 lang=python
#
# [1260] Shift 2D Grid
#

# @lc code=start

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        sequence = []
        output = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sequence.append(grid[i][j])
        k %= len(sequence)
        updated = sequence[-k:] + sequence[:-k]
        count = 0
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(updated[count])
                count += 1
            output.append(temp)
        return output
# @lc code=end
