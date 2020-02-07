#
# @lc app=leetcode id=1343 lang=python
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = sum(arr[0:k])
        count = 1 if (curSum / k) >= threshold else 0
        for pos, val in enumerate(arr[k:]):
            curSum -= arr[pos]
            curSum += val
            if (curSum/k) >= threshold:
                count += 1
        return count

# @lc code=end
