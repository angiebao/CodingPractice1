class Solution:
    # brute force is Time O((m*n)^2)
    # dynamic programming is Time O(m*n), space O(m*n)
    def maximalSquare(self, matrix) -> int:

        row = len(matrix)
        if row ==0:
            return 0
        col = len(matrix[0])
        dp = [[0] * (col+1) for i in range(row + 1)]
        maxlength = 0
        for i in range(1, row+1):
            for j in range(1, col + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxlength = max(maxlength, dp[i][j])
        return maxlength**2

