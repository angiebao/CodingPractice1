class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * (n ) for i in range(n )]
        if n == 0:
            return ""

        maxSub = s[0]
        for i in range(0, n-1):
            dp[i][i] = 1
            dp[i][i + 1] = int(s[i] == s[i+1])
            if dp[i][i + 1] == 1:
                maxSub = s[i:i+2]
        dp[n-1][n-1] = 1

        for i in range(n-3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = (dp[i + 1][j - 1] & (s[i] == s[j]))
                if dp[i][j] == 1 and j -i + 1 > len(maxSub):
                    maxSub = s[i:j+1]

        return maxSub

s= Solution()
print(s.longestPalindrome("abcba"))