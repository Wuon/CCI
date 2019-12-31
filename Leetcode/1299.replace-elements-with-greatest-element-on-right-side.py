#
# @lc app=leetcode id=1299 lang=python
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        output = [largest]
        for i in range(len(arr) -1, 0, -1):
            if arr[i] > largest:
                largest = arr[i]
            output.append(largest)
        return output[::-1]

# @lc code=end
