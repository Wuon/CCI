#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for cur in strs:
            copy = ''.join(sorted(cur))
            if copy in d:
                d[copy].append(cur)
            else:
                d[copy] = [cur]
        return d.values()
# @lc code=end
