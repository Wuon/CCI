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
        area = 0
        front = 0
        back = len(height) - 1
        while front < back:
            curArea = min(height[front], height[back]) * (back - front)
            area = max(curArea, area)
            if height[front] > height[back]:
                back -= 1
            elif height[back] > height[front]:
                front += 1
            else:
                if height[back - 1] > height[back]:
                    back -= 1
                else:
                    front += 1
        return area
# @lc code=end
