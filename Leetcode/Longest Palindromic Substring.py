#TODO optimize
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        for i in range(len(s), -1, -1):
            for j in range(len(s)-i):
                n = s[j:j+i+1]
                if n == n[::-1]:
                    return n
        return ""
