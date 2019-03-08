import re
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        r = re.sub(r'\W+', '', s).lower()
        return r == r[::-1]
