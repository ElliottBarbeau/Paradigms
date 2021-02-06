#Subset sum problem
def solve(arr, M):
    dp = [[False for _ in range(M + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp[i][0] = True
    
    for row in range(1, len(arr) + 1):
        for column in range(1, M + 1):
            if column < arr[row - 1]:
                dp[row][column] = dp[row-1][column]
            else:
                if dp[row-1][column]:
                    dp[row][column] = dp[row - 1][column]
                else:
                    dp[row][column] = dp[row-1][column - arr[row-1]]

    return dp[len(arr)][M]

        
print(solve([5, 2, 1, 3], 9))