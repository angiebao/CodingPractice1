import numpy


class Solution:
    def rob(self, nums) -> int:
        # nr = len(nums)
        # nc = sum(nums) + 1
        # dp = [[0] * (nc + 1) for i in range(nr + 1)]
        # dp = numpy.array(dp)
        # dp[0][0] = 1
        # dp[1][nums[0]] = 1
        #
        # for i in range(2, nr+1):
        #     for j in range(1, nc+1):
        #         if j - nums[i - 1] >= 0 and 1 in dp[0:(i - 1), j - nums[i - 1]]:
        #             dp[i][j] = 1
        #         if j == nums[i - 1]:
        #             dp[i][j] = 1
        #
        # for j in range(nc,-1,-1):
        #     for i in range(nr,-1, -1):
        #         if dp[i][j] == 1:
        #             return j

        nr = len(nums)
        if nr == 0:
            return 0
        dp = [0 for i in range(nr + 1)]  # store maxium rob amout up to current i

        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, nr + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])  # max(rob this house, not rob this house)

        return dp[nr]
nums = [1,2,3,1]
#nums = [2,7,9,3,1]
s = Solution()
print(s.rob(nums))