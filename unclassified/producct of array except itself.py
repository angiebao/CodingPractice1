class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [1] * n
        s = [1] * n
        p[0] = nums[0]
        s[n - 1] = nums[n - 1]
        result = [1] * n
        for i in range(1, n):
            p[i] = p[i - 1] * nums[i]

        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] * nums[i]
        print(p)
        print(s)
        for i in range(n):
            pre = (1 if i - 1 < 0 else p[i - 1])
            suf = (1 if i + 1 > n - 1 else s[i + 1])
            result[i] = pre * suf

        return result