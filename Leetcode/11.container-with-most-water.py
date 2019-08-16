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
        l, r = 0, len(height) - 1
        area = (r - l) * (height[l] if height[l] < height[r] else height[r])
        while l != r:
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            temp = (r - l) * (height[l] if height[l] < height[r] else height[r])
            if temp > area:
                area = temp
        return area
# @lc code=end
