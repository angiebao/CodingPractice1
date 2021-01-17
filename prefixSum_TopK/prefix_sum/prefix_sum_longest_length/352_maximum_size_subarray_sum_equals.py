# Prefix Sum求最长长度
# ‌
# 初始化需要在map中添加(0, -1)
# Key是当前的sum
# Value是当前的index

# 325. Maximum Size Subarray Sum Equals k
# Medium
#
# 1061
#
# 35
#
# Add to List
#
# Share
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
#
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:
#
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?

# public class Q_0325_Maximum_Size_Subarray_Sum_Equals_k {
#
#
#    public static void main(String[] args) {
#        Q_0325_Maximum_Size_Subarray_Sum_Equals_k solution = new Q_0325_Maximum_Size_Subarray_Sum_Equals_k();
#        int[] nums1 = {1, -1, 5, -2, 3};
#        int k1 = 3;
#        int[] nums2 = {-2, -1, 2, 1};
#        int k2 = 1;
#        System.out.println(solution.maxSubArrayLen(nums1, k1));
#        System.out.println(solution.maxSubArrayLen(nums2, k2));
#    }
#
#
#    /*
#    Solution 1: Prefix sum
#     */
#    public int maxSubArrayLen(int[] nums, int k) {
#        Map<Integer, Integer> map = new HashMap<>();
#        map.put(0, -1);
#        int sum = 0;
#        int res = 0;
#        for (int i = 0; i < nums.length; i++) {
#            sum += nums[i];
#            if (map.containsKey(sum - k)) {
#                res = Math.max(res, i - map.get(sum - k));
#            }
#            map.putIfAbsent(sum, i);
#        }
#        return res;
#    }
# }

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maps = dict()
        # use a map to stopre the prefix sum as keys, value is the index in the nums array
        maps[0] = -1  # -1 is used when the index is 0, in case later on,  we have a 0 prefix sum , we still use the -1 index
        sums = 0
        res = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in maps:
                res = max(res, i - maps[sums - k])
            if sums not in maps:
                maps[sums] = i

        return res