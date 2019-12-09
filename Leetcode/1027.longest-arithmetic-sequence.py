#
# @lc app=leetcode id=1027 lang=python
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longest = 0
        if not A:
            return longest
        d = {}
        for i in range(len(A)):
            d[A[i]] = {}
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                if diff in d[A[j]]:
                    d[A[i]][diff] = d[A[j]][diff] + 1
                else:
                    d[A[i]][diff] = 1
                longest = max(longest, d[A[i]][diff])
        return longest + 1
# @lc code=end
