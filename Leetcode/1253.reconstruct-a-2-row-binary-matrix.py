#
# @lc app=leetcode id=1253 lang=python
#
# [1253] Reconstruct a 2-Row Binary Matrix
#

# @lc code=start

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        two = colsum.count(2);
        one = colsum.count(1);
        if two > lower or two > upper:
            return []
        if two * 2 + one != upper + lower:
            return []
        topOne = upper - two
        ds = [[0 for x in range(len(colsum))] for y in range(2)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                ds[0][i] = 1
                ds[1][i] = 1
            elif colsum[i] == 1:
                if topOne != 0:
                    ds[0][i] = 1
                    ds[1][i] = 0
                    topOne -= 1
                else:
                    ds[0][i] = 0
                    ds[1][i] = 1
        return ds
# @lc code=end
