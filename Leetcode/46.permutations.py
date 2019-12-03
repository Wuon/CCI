#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        if not nums:
            return output
        if len(nums) == 1:
            return [nums]
        stack = []
        for i in range(len(nums)):
            stack.append([[nums[i]], nums[:i] + nums[i+1:]])
            while stack:
                cur = stack.pop()
                if not cur[1]:
                    output.append(cur[0])
                else:
                    for j in range(len(cur[1])):
                        stack.append([cur[0] + [cur[1][j]], cur[1][:j] + cur[1][j+1:]])
        return output



# @lc code=end
