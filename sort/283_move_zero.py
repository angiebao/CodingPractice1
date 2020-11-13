class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # buble sort is stable sort, the rest of array's order remains unchanged
        # time O(n^2), space O(1)

        # for i in range(0, len(nums)-1):
        #     for j in range(0, len(nums)-1-i):   #O(n + n-1 +n-2 + ....1)= O(n^2)
        #         if nums[j]==0:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1]=temp

        # two pointer method
        # time O(n) space O(1)
        avail = 0
        current = 0
        for current in range(0, len(nums)):
            if nums[current] != 0:
                nums[current], nums[avail] = nums[avail], nums[current]
                avail += 1

        for i in range(avail, len(nums)):
            nums[i] = 0