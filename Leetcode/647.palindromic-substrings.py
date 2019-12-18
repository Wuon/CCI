#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        dp = [[None for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            counter += 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                    counter += 1
        return counter
# @lc code=end
