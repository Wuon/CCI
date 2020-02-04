#
# @lc app=leetcode id=1338 lang=python
#
# [1338]  Reduce Array Size to The Half
#

# @lc code=start

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for item in arr:
            if item not in freq:
                freq[item] = 0
            freq[item] += 1
        target = len(arr) // 2
        new = reversed(sorted(freq, key=freq.get))
        count = 0
        for item in new:
            count += 1
            target -= freq[item]
            if target <= 0:
                return count
        return count

# @lc code=end
