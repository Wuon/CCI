#
# @lc app=leetcode id=939 lang=python
#
# [939] Minimum Area Rectangle
#

# @lc code=start
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        minArea = float('inf')
        d = {}
        for i in range(len(points)):
            first = points[i]
            for j in range(i + 1, len(points)):
                second = points[j]
                if first[0] == second[0]:
                    pair = (first[1], second[1])
                    if pair in d:
                        deltaX = second[0] - d[pair][0]
                        deltaY = second[1] - d[pair][1]
                        minArea = min(minArea, abs(deltaX * deltaY))
                    d[pair] = first
                else:
                    break
        return 0 if minArea == float('inf') else minArea

# @lc code=end
