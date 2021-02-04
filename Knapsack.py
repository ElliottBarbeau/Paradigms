#Knapsack
class KnapsackProblem:
    def __init__(self, n, M, wt, v):
        self.n = n
        self.M = M
        self.wt = wt
        self.v = v
        self.dp = [[0 for _ in range(self.M + 1)] for _ in range(self.n + 1)]

    def solve(self):
        for i in range(self.n + 1):
            for w in range(self.M + 1):
                if i == 0 or w == 0:
                    self.dp[i][w] = 0
                elif self.wt[i-1] <= w:
                    self.dp[i][w] = max(self.dp[i-1][w], self.v[i-1] + self.dp[i-1][w - self.wt[i-1]])
                else:
                    self.dp[i][w] = self.dp[i-1][w]

        return self.dp[self.n][self.M]


if __name__ == '__main__':
    knapsack = KnapsackProblem(3, 6, [1, 2, 3], [10, 15, 40])
    print(knapsack.solve())