class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)):
        #     item1= nums[i]
        #     for j in range(i+1,len(nums)):
        #         item2 = nums[j]
        #         if item1 + item2 == target:
        #             return [i, j]
        d = dict()
        for i in range(0, len(nums)):
            d[nums[i]] = i # the later one will replace the previous ones' index

        for i in range(0, len(nums)):
            if (target - nums[i]) in d and d[target - nums[i]] != i:
                return [d[target - nums[i]], i]

        if i == len(nums):
            return []