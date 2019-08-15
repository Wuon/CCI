#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        ans = ''
        dp = [[None] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            ans = s[i]
            longest = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
                longest = 2
        for j in range(len(s)):
            for i in range(0, j-1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if longest < j - i + 1:
                        longest = j - i + 1
                        ans = s[i:j+1]
        return ans
# @lc code=end
