# k = 6
# 1 2 3 4
# 5 6 7 8 9 10 11 12 13

# (1 2 3) 4
# (5 6 7) 8 9 10 11 12 13

# k- k//2 = 3

# 3//2 = 1
# 4
# (5 ) 6 7 8 9 10 11 12 13


# 1 2 3 4) 5 6 7 8 9
# 10 11 12 13) 14 15 16 17 18


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (self.findkth(nums1, nums2, n // 2) + self.findkth(nums1, nums2, n // 2 + 1)) / 2
        else:
            return self.findkth(nums1, nums2, n // 2 + 1)

    def findkth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        if len(nums1) < k // 2:
            return self.findkth(nums1, nums2[k // 2:], k - k // 2)
        if len(nums2) < k // 2:
            return self.findkth(nums1[k // 2:], nums2, k - k // 2)

        if nums1[k // 2 - 1] < nums2[k // 2 - 1]:
            return self.findkth(nums1[k // 2:], nums2, k - k // 2)
        else:
            return self.findkth(nums1, nums2[k // 2:], k - k // 2)
