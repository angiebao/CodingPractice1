# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = start + math.floor((end - start) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end]:  # sort in right
                # it is not garenteed that target is with in mid to end, because the entire arry is not sorted
                # if target not in the sorted right part, it will lie in the left part
                if nums[mid] < target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

            elif nums[mid] > nums[start]:  # sort in left
                # if target not in the sorted right part, it will laies in the left part
                if  nums[start] <= target and target <nums[mid]  :
                    end = mid
                else:
                    start = mid

        if (nums[start] == target):
            return start
        elif (nums[end] == target):
            return end
        else:
            return -1



# def search(nums, target):
#     start =
#     end =
#     while start + 1 < end:
#         mid =
#     # find in the left sorted array
#         if nums[mid]<nums[end]:
#             if nums[mid] < target and target <= nums[end]:
#                 start = mid
#             else:
#                 end = mid
#
#         # find in the right sorted array
#         if nums[mid] > nums[start]:
#             if nums[start]<= target and target < nums[mid] :
#                 end = mid
#             else:
#                 start = mid
#
#
#
#         if nums[mid] == target:
#             return True


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # if mid lies in the right montone increase interval
        # if target lies in the mid-right, take the right part, otherwise take the left
        # 4 5 6 7 (0 1 2 3)

        # if mid lies in the left monotone increase interval
        # if target lies in the left-mid take the left part, otherwise take the right part
        # (4 5 6 7) 0 1 2 3
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if (nums[mid] < nums[right] and nums[mid] < target <= nums[right]) or \
                    (nums[mid] >= nums[right] and not (nums[left] <= target < nums[mid])):
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1