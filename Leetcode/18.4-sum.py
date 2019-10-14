#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = {}
        output = []
        nums.sort()
        for i, w in enumerate(nums):
            for j, x in enumerate(nums[i + 1:]):
                val = target - w - x
                if val not in d:
                    d[val] = [(i,j + i + 1)]
                else:
                    d[val].append((i,j + i + 1))
        for i, y in enumerate(nums):
            for j, z in enumerate(nums[i + 1:]):
                val = y + z
                if val in d:
                    for pair in d[val]:
                        if len(set([pair[0], pair[1], i, j + i + 1])) == 4:
                            output.append([nums[pair[0]], nums[pair[1]], nums[i], nums[j + i + 1]])
        return set(tuple(sorted(x)) for x in output)
# @lc code=end
