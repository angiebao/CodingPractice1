# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
# of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

# public class Q_0209_Minimum_Size_Subarray_Sum {
#
#
#    public static void main(String[] args) {
#        Q_0209_Minimum_Size_Subarray_Sum solution = new Q_0209_Minimum_Size_Subarray_Sum();
#        int[] nums = {2,3,1,2,4,3};
#        int s = 7;
#        System.out.println(solution.minSubArrayLen(s, nums));
#    }
#
#
#    public int minSubArrayLen(int s, int[] nums) {
#        int start = 0;
#        int end = 0;
#        int sum = 0;
#        int res = Integer.MAX_VALUE;
#        while (end < nums.length) {
#            sum += nums[end];
#            end++;
#            while (start < end) {
#                if (sum >= s) {
#                    res = Math.min(res, end-start);
#                    sum -= nums[start];
#                    start++;
#                } else {
#                    break;
#                }
#            }
#        }
#        return res == Integer.MAX_VALUE ? 0 : res;
#    }
# }

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        sums = 0
        res = float('inf')
        while (end < len(nums)):
            sums += nums[end]
            end += 1
            while start < end:
                if sums >= s:
                    res = min(res, end - start)
                    sums -= nums[start]
                    start += 1
                else:
                    break

        return res if res != float('inf') else 0