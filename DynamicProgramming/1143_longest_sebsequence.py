# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# A subsequence of astring is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order of the remaining characters.(eg, "ace" is a subsequence of "abcde"
# while "aec" is not).A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence,
# return 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) + 1
        m = len(text2) + 1
        dp = [[0] * m for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[n - 1][m - 1]


text1 = "abcde"
text2 = "ace"