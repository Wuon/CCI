#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            moves += nums[i] - nums[0]
        return moves
# @lc code=end

