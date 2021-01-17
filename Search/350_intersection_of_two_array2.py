class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # method 1 use two pointer
        # method 2 use binary search as follows
        nums1.sort()
        nums2.sort()
        res = []
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        i = 0
        while i < (len(nums1)):
            cnt1 = 1
            while i + 1 < len(nums1) and nums1[i] == nums1[i + 1]:
                i += 1
                cnt1 += 1

            cnt2 = self.countTargetArray2(nums2, nums1[i])
            print("cnt1, cnt2, ", cnt1, cnt2)
            for j in range(0, min(cnt1, cnt2)):
                res.append(nums1[i])

            i += 1
        return res

    def countTargetArray2(self, nums2, target):
        lower = self.findBoundary(nums2, target, True)
        if lower == -1:
            return 0
        upper = self.findBoundary(nums2, target, False)

        return upper - lower + 1

    def findBoundary(self, nums, target, lower):
        start = 0
        end = max(len(nums) - 1, 0)
        while start + 1 < end:
            mid = start + math.floor((end - start) / 2)
            # find the lower bond
            if lower:
                if target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target:
                    start = mid
                else:
                    end = mid

        if lower:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1

        else:
            if nums[end] == target:
                return end
            elif nums[start] == target:
                return start
            else:
                return -1