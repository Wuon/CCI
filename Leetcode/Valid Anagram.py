class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        store = [0] * 26
        for c in s:
            store[ord(c) - 97] += 1
        for c in t:
            store[ord(c) - 97] -= 1
        for i in store:
            if i != 0:
                return False
        return True
