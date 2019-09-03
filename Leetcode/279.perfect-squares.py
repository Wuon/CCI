#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        for i in range(1,int(math.sqrt(n))+1):
            squares.append(math.pow(i, 2))
        level = 0
        cur = [0]
        while True:
            nxt = []
            for val in cur:
                for square in squares:
                    if val + square == n:
                        return level + 1
                    if val + square < n:
                        nxt.append(val + square)
            cur = list(set(nxt))
            level += 1
# @lc code=end
