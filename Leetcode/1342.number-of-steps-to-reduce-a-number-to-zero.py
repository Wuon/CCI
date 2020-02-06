#
# @lc app=leetcode id=1342 lang=python
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return count

# @lc code=end
