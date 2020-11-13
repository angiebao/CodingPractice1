class Solution:
    def maxProfit(self, prices) -> int:
        # state transition equation
        # dp[i][k][0]= max(dp[i-1][k][0], dp[i-1][k][1] +  prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        # time O(N), space O(2N+2n) = O(N)
        n = len(prices)
        dp_k1 = [[0] * 2 for i in range(n + 1)]
        dp_k2 = [[0] * 2 for i in range(n + 1)]

        dp_k1[0][1] = float('-inf')
        dp_k1[0][0] = 0
        dp_k2[0][0] = 0
        dp_k2[0][1] = - prices[0]

        for i in range(1, n + 1):
            dp_k2[i][0] = max(dp_k2[i - 1][0], dp_k2[i - 1][1] + prices[i - 1])
            dp_k2[i][1] = max(dp_k2[i - 1][1], dp_k1[i - 1][0] - prices[i - 1])

            dp_k1[i][0] = max(dp_k1[i - 1][0], dp_k1[i - 1][1] + prices[i - 1])
            dp_k1[i][1] = max(dp_k1[i - 1][1],  - prices[i - 1])



        return max(dp_k1[n][0], dp_k2[n][0])

       # time O(n), space O(1)
        # dp_i10 = 0
        # dp_i11 = float('-inf')
        # dp_i20 = 0
        # dp_i21 = float('-inf')
        # for i in range(len(prices)):
        #     dp_i20 = max(dp_i20, dp_i21 + prices[i])
        #     dp_i21 = max(dp_i21, dp_i10 - prices[i])
        #     dp_i10 = max(dp_i10, dp_i11 + prices[i])
        #     dp_i11 = max(dp_i11, -prices[i])
        #
        # return dp_i20


s= Solution()
print(s. maxProfit([3,3,5,0,0,3,1,4]))