class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        store = [0] * 26
        for c in s:
            store[ord(c) - 97] += 1
        for i in range(0, len(s)):
            if store[ord(s[i]) - 97] == 1:
                return i
        return -1
