class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #         d = dict()
        #         for item in nums:
        #             if item not in d:
        #                 d[item] = 1
        #             else:
        #                 d[item]+=1

        #         for k, v in d.items():
        #             if v == 1:
        #                 return k
        item0 = nums[0]
        for item in nums[1:]:
            item0 = item0 ^ item

        return item0