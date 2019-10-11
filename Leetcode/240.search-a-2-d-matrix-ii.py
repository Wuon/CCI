#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        x = 0
        y = len(matrix) - 1
        while 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                y -= 1
            else:
                x += 1
        return False
# @lc code=end
