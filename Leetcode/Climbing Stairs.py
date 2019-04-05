class Solution:
    def climbStairs(self, n: int) -> int:
        fib = n + 2
        if fib == 1:
            return 1
        a = [0] * fib
        a[0] = 0
        a[1] = 1
        for i in range(1, fib-1):
            a[i+1] = a[i] + a[i-1]
        return a[len(a) - 1]
