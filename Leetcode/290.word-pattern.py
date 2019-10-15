#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) == 0:
            return False
        d = {}
        s = set()
        sequence = str.split(" ")
        if len(pattern) != len(sequence):
            return False
        for i, char in enumerate(pattern):
            if char not in d:
                if sequence[i] not in s:
                    s.add(sequence[i])
                    d[char] = sequence[i]
                else:
                    return False
            else:
                if d[char] != sequence[i]:
                    return False
        return True

# @lc code=end
