# 491. Increasing Subsequences
# Medium
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.
#
#
#
# Example:
#
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
#
# Note:
#
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.


def dfs(i, n, nums, cur, res):
    if i == n:
        if cur not in res and len(cur) >= 2:
            res.append(cur[:])
        return

        # if the currentlist is entirely less than the numbers after the current index in nums
    if not cur or cur[-1] <= nums[i]:
        cur.append(nums[i])
        dfs(i + 1, n, nums, cur, res)
        cur.pop()

    dfs(i + 1, n, nums, cur, res)


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        i = 0
        res = []
        dfs(0, n, nums, [], res)

        return res