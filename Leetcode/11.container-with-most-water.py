#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0
        l = 0
        r = len(height) - 1
        while l < r:
            largest = max(largest, min(height[l], height[r]) * (r - l))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return largest
# @lc code=end
