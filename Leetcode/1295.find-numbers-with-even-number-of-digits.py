#
# @lc app=leetcode id=1295 lang=python
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                total += 1
        return total

# @lc code=end
