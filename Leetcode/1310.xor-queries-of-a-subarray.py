#
# @lc app=leetcode id=1310 lang=python
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        for query in queries:
            output.append(arr[query[1]] ^ arr[query[0] - 1] if query[0] > 0 else arr[query[1]])
        return output

# @lc code=end
