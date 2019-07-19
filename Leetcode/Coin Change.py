class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        upper = amount + 1
        dp = [upper for i in range(upper)]
        dp[0] = 0
        for i in range(1, upper):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        print(dp)
        return -1 if dp[amount] > amount else dp[amount]
