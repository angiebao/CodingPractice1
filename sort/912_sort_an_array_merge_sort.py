class Solution:
    # merge sort
    def sortArray(self, nums) :
        n = len(nums)
        if n <= 1:
            return nums
        arr1 = nums[0:n // 2]
        arr2 = nums[n // 2:n]

        arr1 = self.sortArray(arr1)
        arr2 = self.sortArray(arr2)
        return self.merge(arr1, arr2)
    
    # time complexity :
    def merge(self, arr1, arr2):
        p1 = 0
        p2 = 0
        arr = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                arr.append(arr1[p1])
                p1 += 1
            else:
                arr.append(arr2[p2])
                p2 += 1
        while p1 < len(arr1):
            arr.append(arr1[p1])
            p1 += 1
        while p2 < len(arr2):
            arr.append(arr2[p2])
            p2 += 1
        return arr
