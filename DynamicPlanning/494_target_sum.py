# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

class Solution:
    # Simple recursive
    # time O(2^N) space O(N), because N layers of recursive function, each layer stores a different value.

    # def findTargetSumWays(self, nums, S: int) -> int:
    #     self.nums = nums
    #     self.count = 0
    #     self.calcSums(-1, 0, 0, S)
    #     return self.count
    #
    # def calcSums(self, index, item, sums, target):

    # sums += item
    #         if sums == target and index == len(self.nums) - 1:
    #             self.count += 1

    #         if index >= len(self.nums) - 1:
    #             return
    #         self.calcSums(index + 1, +self.nums[index + 1], sums, target)  # left tree
    #         self.calcSums(index + 1, -self.nums[index + 1], sums, target)  # right tree


    # save a memeory when at the state (index,  sum) with value of count of methods to reach target
    # time < O(2^N), space
    def findTargetSumWays_recr(self, nums, S: int) -> int:
        self.nums = nums
        self.mem = dict()

        count = self.calcSums(-1, 0, 0, S)
        return count

    def calcSums(self, index, item, sums, target):
        sums += item
        if (index, sums) in self.mem:
            return self.mem[(index, sums)]
        if index >= len(self.nums) - 1:
            return int(sums == target)
        count = self.calcSums(index + 1, +self.nums[index + 1], sums, target) +\
                self.calcSums(index + 1, -self.nums[index + 1], sums, target)  # left tree + right tree
        self.mem[(index, sums)] = count
        return count

    # dynamic programming
    # time: O(N*M), space O(N*M)
    def findTargetSumWays(self, nums, S: int) -> int:
        lenC = sum(nums)*2 + 1  # create the matrix with column number = [-sum, sum]
        lenR = len(nums) + 1
        dp =[[0]*lenC for i in range (lenR)]
        if S> sum(nums):
            return 0
        origon = sum(nums)
        dp[0][origon] = 1

        for i in range(1, lenR):
            for j in range(lenC):
                if j - nums[i-1] >= 0 and dp[i-1][j - nums[i-1]] != 0:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
                if j + nums[i-1] < lenC and dp[i-1][j + nums[i-1]] != 0:
                    dp[i][j] += dp[i-1][j + nums[i-1]]


        return (dp[lenR-1][origon + S])

nums = [1, 1, 1, 1, 1]
target = 3

# nums =[1,0]
# target = 1

# nums = [5, 2, 3]
# target = 10

# nums = [1,2,1]
# target = 0

s=  Solution()
print(s.findTargetSumWays(nums, target))