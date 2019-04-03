class Solution:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        d = 0
        for i in range(32):
            xb = x >> i & 1
            xy = y >> i & 1
            if xb != xy:
                d += 1
        return d
