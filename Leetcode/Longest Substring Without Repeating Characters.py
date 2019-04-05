class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        d = set()
        f, b, m = 0, 0, 0
        while f < len(s) and b < len(s):
            if s[f] not in d:
                d.add(s[f])
                f += 1
                m = f - b if f - b > m else m
            else:
                d.discard(s[b])
                b += 1
        return m
