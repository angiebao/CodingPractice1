# prefix_sum sum method time O(N), Space O(2N)=O(N)
#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        d = dict()
        d[0] = 0
        result = 0
        sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
            d[sums[i + 1]] = i + 1

        maxLength = 0
        for i in range(len(sums)):

            if sums[i] in d:
                maxLength = d[sums[i]] - i
            if maxLength > result:
                result = maxLength

        return result