#
# @lc app=leetcode id=1296 lang=python
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k !=  0:
            return False
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        while d:
            x = min(d)
            for i in range(k):
                if x + i not in d:
                    return False
                else:
                    d[x+i] -= 1
                    if d[x+i] == 0:
                        del d[x+i]
        return True

# @lc code=end
