#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t == 0 and len(nums) == len(set(nums)):
            return False
        d = {}
        for i, num in enumerate(nums):
            for key in d.keys():
                if key - t <= num <= key + t:
                    if abs(i - d[key]) <= k:
                        return True
            d[num] = i
        return False

# @lc code=end
