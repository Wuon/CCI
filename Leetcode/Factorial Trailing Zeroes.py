class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 1
        count = 0
        while 5 ** i <= n:
            count += n // (5**i)
            i += 1
        return count
