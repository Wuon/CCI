import math


class Solution(object):
    def hammingWeight(self, n):
        if n == 0:
            return 0
        x = int(math.ceil(math.log(n, 2)))
        t = 0
        for i in range(x, -1, -1):
            if n - math.pow(2, i) >= 0:
                t += 1
                n -= math.pow(2, i)
        return t
