# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums) -> int:
        # O(N^2)
        #         maxValue = float('-inf')
        #         length = len(nums)
        #         sums = 0
        #         if length == 1:
        #             return nums[0]

        #         for i in range(0, length):
        #             sums = nums[i]
        #             if sums > maxValue:
        #                 maxValue = sums
        #             for j in range(i+1, length):
        #                 sums += nums[j]
        #                 if sums > maxValue:
        #                     maxValue = sums

        #         return maxValue
        # O(N) greedy algorithm/ divide and conquer
        maxValue = float('-inf')
        sums = 0
        length = len(nums)
        if length == 1:
            return nums[0]
        for i in range(0, length):
            sums += nums[i]
            if sums > maxValue:
                maxValue = sums
            if sums < 0:
                sums = 0

        return maxValue


s = Solution()
print(s.maxSubArray([-2,-1]))