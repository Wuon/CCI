#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        if len(height) == 0:
            return total
        left = [0]
        right = 0
        for i in range(len(height)):
            left.append(max(left[i], height[i]))
        for i in range(len(height) - 1, -1, -1):
            right = max(right, height[i])
            if min(left[i], right) > height[i]:
                total += min(left[i], right) - height[i]
        return total
# @lc code=end
