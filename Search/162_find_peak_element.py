# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
import math
# keep pushing the element towards end with the condition that the next element if larger than the current element
# finally if we meet an element that its next element is smaller than the current one, we found one peak .

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + math.floor((end - start) / 2)
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        return start if nums[start] > nums[end] else end