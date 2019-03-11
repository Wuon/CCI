class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        min_s = min(strs)
        for i in range (0, len(min_s)):
            for s in strs:
                if s[i] != min_s[i]:
                    return min_s[:i]
        return min_s
