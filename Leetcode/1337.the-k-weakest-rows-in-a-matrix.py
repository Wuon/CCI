#
# @lc app=leetcode id=1337 lang=python
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = {}
        for i, row in enumerate(mat):
            count = 0
            for item in row:
                if item == 1:
                    count += 1
            output[i] = count
        return (sorted(output, key=output.get)[:k])

# @lc code=end
