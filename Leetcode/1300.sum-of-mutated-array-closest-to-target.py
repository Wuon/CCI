#
# @lc app=leetcode id=1300 lang=python
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        total = 0
        arr.sort()
        for num in arr:
            total += num
        if total == target:
            return arr[-1]
        if round(target / len(arr)) <= arr[0]:
            return round(target / len(arr))
        pos = 0
        optimal = round(target / len(arr))
        for num in arr:
            if num <= optimal:
                target -= num
                pos += 1
        return round(target / (len(arr) - pos))

# @lc code=end
