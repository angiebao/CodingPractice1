class Solution:
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