# there is duplicate numbers in candidates
#each element can use only once
# cannot have repeated list in result

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        start = 0
        sums = 0
        candidates.sort()
        self.helper(candidates, start, sums, target, temp, res)
        return res

    def helper(self, nums, start, sums, target, temp, res):
        if sums > target:
            return
        if sums == target:
            res.append(temp[:])
            return

        for i in range(start, len(nums)):

            if i > start and nums[i] == nums[i - 1]:
                # ensure no duplicate list in the list
                continue
            temp.append(nums[i])
            # will not use one element twice
            self.helper(nums, i + 1, sums + nums[i], target, temp, res)

            temp.pop()

