# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums

        deq = collections.deque()

        def clean_deque(i):
            if deq and i - k >= 0 and deq[0] == nums[i - k]:
                # pop from left
                deq.popleft()

            while deq and nums[i] > deq[-1]:
                deq.pop()

        max_idx = 0
        # initialize the deque
        for i in range(k):
            clean_deque(i)
            deq.append(nums[i])
            # compute the max in nums[0:k]
            if nums[i] > nums[max_idx]:
                max_idx = i

        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deque(i)
            deq.append(nums[i])
            output.append(deq[0])

        return output
