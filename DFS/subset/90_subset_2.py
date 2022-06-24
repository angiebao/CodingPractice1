# have duplicate numberes, but output should not contain duplicate subset
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        start = 0
        nums.sort()
        self.helper(nums, start, temp, res)

        return res

    def helper(self, nums, start, temp, res):
        res.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.helper(nums, i + 1, temp, res)
            temp.pop()

#             while i < len(nums)-1 and nums[i] == nums[i+1]:
#                 next(itr)
#                 i += 1


[1, 2, 2]
Res = [[1], [1,2], [1,2,2] ]
Temp = [1, 2, 2], [1,2]  ,
Start = 0, 1, 2,   1,

start = 0,  1, 2
temp =  [1], [1,2], [1,2,2] ,

start = 1


start = 2