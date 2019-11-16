#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroPointer = 0
        twoPointer = len(nums)-1
        i = 0
        while i <= twoPointer:
            if nums[i] == 0:
                nums[i], nums[zeroPointer] = nums[zeroPointer], nums[i]
                zeroPointer += 1
            elif nums[i] == 2:
                nums[i], nums[twoPointer] = nums[twoPointer], nums[i]
                twoPointer -= 1
                i -= 1
            i += 1
# @lc code=end
