def longestCommonSubstring(s, t):
    largest = 0
    dp = [[0 for i in range(len(s))] for j in range(len(t))] 
    for i in range(len(t)):
        for j in range(len(s)):
            value = 1 if t[i] == s[j] else 0
            if value == 1 and i > 0 and j > 0:
                value += dp[i-1][j-1]
            dp[i][j] = value
            largest = max(largest, dp[i][j])
    return largest
