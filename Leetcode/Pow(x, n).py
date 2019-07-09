class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        return x * self.myPow(x, n - 1) if n % 2 != 0 else self.myPow(x*x, n/2) if n else 1
