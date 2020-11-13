# class Solution(object):
#     # 有多少种, Dynamic programming
#     # 罗列出所有中方法 BFS
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         self.result = 0
#         self.dfs(nums, S, 0, 0)
#         return self.result
#     def dfs(self, nums, S, cur, i):
#         if i==len(nums):

#             self.result += int(cur == S)

#             return

#         self.dfs(nums, S, cur + nums[i], i+1)

#         self.dfs(nums, S, cur - nums[i], i+1)

class Solution(object):
    # 有多少种, Dynamic programming
    # 罗列出所有中方法 BFS
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        memo = {}
        return self.dfs(nums, S, 0, 0, memo)

    def dfs(self, nums, S, cur, i, memo):
        if i == len(nums):
            return int(cur == S)

        if (i, cur) in memo:
            result = memo[(i, cur)]
            return result

        result1 = self.dfs(nums, S, cur + nums[i], i + 1, memo)

        result2 = self.dfs(nums, S, cur - nums[i], i + 1, memo)

        result = result1 + result2

        memo[(i, cur)] = result

        return result

nums= [6,44,30,25,8,26,34,22,10,18,34,8,0,32,13,48,29,41,16,30]
S=12
s= Solution()
result = s.findTargetSumWays(nums, S)
print(result)