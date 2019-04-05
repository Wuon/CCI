class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        s = set()
        o = 0
        for i in range(2, n):
            if i not in s:
                x = i
                while x <= n:
                    s.add(x)
                    x += i
                o += 1
        return o
