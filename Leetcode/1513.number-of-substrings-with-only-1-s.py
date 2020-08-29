#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        def generate(n):
            possibility = 0
            for i in range(n):
                possibility += (i + 1)
            return possibility
        result = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] == '0':
                start += 1
                end += 1
            else:
                while end < len(s) and s[end] == '1':
                    end += 1
                diff = end - start
                start = end
                result += generate(diff)
        return result % (10**9 + 7)
# @lc code=end

