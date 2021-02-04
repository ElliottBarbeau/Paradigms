#Rod Cutting
def solve(n, p):
    dp = [[0]*(n + 1) for _ in range(len(p))]
    for i in range(1, len(p)):
        for j in range(1, n + 1):
            if i <= j:
                dp[i][j] = max(dp[i-1][j], p[i] + dp[i][j-i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(p)-1][n]

print(solve(5, [0, 2, 5, 7, 3, 9]))