#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        se = set()
        for word in wordDict:
            se.add(word)
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True

        for i in range(1, length + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j: i] in se:
                    dp[i] = True
                    break
        return dp[length]
# @lc code=end
