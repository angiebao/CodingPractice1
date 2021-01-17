# Input: nums = [1,3,5,6], target = 5
# Output: 2
# if not distinct, return the left position
# [1,2,8,8,8,10] , target 8,
# outout 2

import math
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while (low + 1 < high):
            mid = low + math.floor((high - low)/2)
            if nums[mid]> target:
                high = mid
            elif nums[mid] < target:
                low = mid
            else:
                high= mid
        # test the three condition that target laies less than low, in between low and high, or larger than high
        if target <= nums[low]:
            return low
        elif target <= nums[high]:
            return high
        else:
            return high + 1
