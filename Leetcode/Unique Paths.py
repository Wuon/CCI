class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(m)] for y in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(m):
            dp[0][i] = 1
        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[n - 1][m - 1]
