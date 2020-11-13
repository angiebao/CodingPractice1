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