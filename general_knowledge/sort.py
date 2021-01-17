# merge sort
class Solution:
    def merge_sort(self, nums):
        pass
    def helper(self, nums, i, j):
        if i>=j:
            return
        mid = (i + j) //2
        #[i, mid] and [mid + 1, j]
        self.helper(nums, i, mid)
        self.helper(nums, mid + 1, j)

        temp, index1, index2 = [], i, mid+ 1

        while  index1 <= mid and index2 <= j:
            if nums[index1] < nums[index2]:
                temp.append(nums[index1])
                index1 +=1
            else:
                temp.append(nums[index2])
                index2 += 1
        temp.extend(nums[index1: mid + 1])
        temp.extend(nums[index])
