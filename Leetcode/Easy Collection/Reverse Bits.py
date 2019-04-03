class Solution:
    def reverseBits(self, n):
        d = []
        o = 0
        for i in range(32):
            d.append(n >> i & 1)
        for b in d:
            o = (o << 1) | b
        return o
