# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
class Solution:
    #    def subarraySum(self, nums: List[int], k: int) -> int:
    #         n= len(nums)
    #         sums = [0 for i in range(n+1)]
    #         sums[0] = 0
    #         count = 0
    #         sum
    #         for i in range(1, n+1):
    #             sums[i] = sums[i-1] + nums[i-1]
    #             #print(sums[i])

    #         for i in range(0, n+1):
    #             for j in range(i+1, n+1):
    #                 result = sums[j] - sums[i]
    #                 #print(sums[i][j])
    #                 if result ==k:
    #                     count +=1

    #         return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        # save the prefix sum, calcualte x-prefixsum = k, check if x = prefisum+k exist in the prefix sum dictionary.
        n = len(nums)
        sums = collections.defaultdict(int)
        prefixSum = 0
        prefixSumArr = [0]

        for i in range(n):
            prefixSum += nums[i]
            sums[prefixSum] += 1
            prefixSumArr.append(prefixSum)

        count = 0
        for i in range(1, n + 1):
            target = k + prefixSumArr[i - 1]
            count += sums[target]

            if sums[prefixSumArr[i]]:  # only check prefix sum after the ith prefix sum
                sums[prefixSumArr[i]] -= 1

        return count