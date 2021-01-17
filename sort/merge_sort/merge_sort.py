# nums is List[int]
class Solution1:

    def sortArray(self, nums):
        temp = [0 for _ in range(len(nums))]
        self.merge_sort(nums, 0, len(nums) -1, temp)
        return temp

    def merge_sort(self, nums, left, right, temp):
        if left >= right:
            return

        mid = (left + right)//2
        self.merge_sort(nums, left, mid, temp)
        self.merge_sort(nums, mid + 1, right, temp)
        self.merge(nums, left, mid, right, temp)

    def merge(self, nums, left, mid, right, temp):
        # left = start
        # right = mid + 1
        # index = start

        index1, index2 = left, mid + 1

        while index1 <= mid and index2 <= right:
            if nums[index1]< nums[right]:
                temp[index1] = nums[index1]
                index1 +=1
            else:
                temp[index1] = nums[index2]
                index2 +=1

        temp.extend(nums[index1:mid+1])
        temp.extend(nums[index2:right+1])

        nums[left :right+1] == temp




class Solution2:
    def sortIntegers2(self, A):
        temp = [0 for _ in range(len(A))]
        self.merge_sort(A, 0, len(A) - 1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        mid = start + (end - start) // 2
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid + 1, end, temp)
        self.merge(A, start, mid, end, temp)

    def merge(self, A, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1
        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1
        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1

        for index in range(start, end + 1):
            A[index] = temp[index]

nums = [2, 3, 5, 3, 1, 4, 7]
s = Solution2()
s.sortIntegers2(nums)
print(nums)