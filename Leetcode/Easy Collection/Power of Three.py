import math


class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        return math.pow(3, math.ceil(math.log(n, 3))) == n
