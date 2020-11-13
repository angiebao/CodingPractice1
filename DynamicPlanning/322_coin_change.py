class Solution:
    def coinChange(self, coins, amount: int) -> int:

        nr = len(coins)
        nc = amount

        dp = [[0] * (nc + 1) for i in range(nr + 1)]

        dp[0][0] = 1

        for i in range(1, nr + 1):
            for j in range(1, nc + 1):
                if j - coins[i - 1] ==0:
                    dp[i][j] = 1
                if j - coins[i - 1] >= 0 and dp[i - 1][j - coins[i - 1]] > 0:
                    dp[i][j] = dp[i - 1][j - coins[i - 1]] + (1 + (-1) * int(i-1==0)*int(j - coins[i - 1]==0))

                if j - coins[i - 1] >= 0 and dp[i][j - coins[i - 1]] > 0:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, max(int(dp[i][j] != 0) * dp[i][j], int(dp[i][j] == 0) * float('inf')))

                if dp[i - 1][j] > 0:
                    dp[i][j] = min(dp[i - 1][j], max(int(dp[i][j] != 0) * dp[i][j], int(dp[i][j] == 0) * float('inf')))

        if dp[nr][amount] ==0:
            return -1
        return dp[nr][amount]


coins= [1,2,5]
amount = 11
coins = [2]
amount = 3

coins = [1,2]
amount = 2
s = Solution()
print(s.coinChange(coins, amount))