# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination_path_finding, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    # TIME O(N^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp stores the value for the current longest increasing sebsequence, so initlialy, each has at least 1
        # time O(n^2), use binary search, could be O(Nlog N)
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

# binary search O(NlogN)
# public int lengthOfLIS(int[] nums) {
#     int[] top = new int[nums.length];
#     // 牌堆数初始化为 0
#     int piles = 0;
#     for (int i = 0; i < nums.length; i++) {
#         // 要处理的扑克牌
#         int poker = nums[i];

#         /***** 搜索左侧边界的二分查找 *****/
#         int left = 0, right = piles;
#         while (left < right) {
#             int mid = (left + right) / 2;
#             if (top[mid] > poker) {
#                 right = mid;
#             } else if (top[mid] < poker) {
#                 left = mid + 1;
#             } else {
#                 right = mid;
#             }
#         }
#         /*********************************/

#         // 没找到合适的牌堆，新建一堆
#         if (left == piles) piles++;
#         // 把这张牌放到牌堆顶
#         top[left] = poker;
#     }
#     // 牌堆数就是 LIS 长度
#     return piles;
# }

