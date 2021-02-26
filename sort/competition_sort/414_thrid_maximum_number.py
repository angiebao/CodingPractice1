# Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
#
#
#
# Example 1:
#
# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.
# Example 2:
#
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
#
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# Follow up: Can you find an O(n) solution?



#
# public class Q_0414_Third_Maximum_Number {
#
#
#    public static void main(String[] args) {
#        Q_0414_Third_Maximum_Number solution = new Q_0414_Third_Maximum_Number();
#        int[] nums1 = {3,2,1};
#        int[] nums2 = {1,2};
#        int[] nums3 = {2,2,3,1};
#        System.out.println(solution.thirdMax(nums1));
#        System.out.println(solution.thirdMax(nums2));
#        System.out.println(solution.thirdMax(nums3));
#    }
#
#
#    public int thirdMax(int[] nums) {
#        Integer max1 = null;
#        Integer max2 = null;
#        Integer max3 = null;
#        for (Integer num : nums) {
#            if (num.equals(max1) || num.equals(max2) || num.equals(max3)) {
#                continue;
#            }
#            if (max1 == null || num > max1) {
#                max3 = max2;
#                max2 = max1;
#                max1 = num;
#            } else if (max2 == null || num > max2) {
#                max3 = max2;
#                max2 = num;
#            } else if (max3 == null || num > max3) {
#                max3 = num;
#            }
#        }
#
#
#        // if there are at least three elements -> return max3
#        // if there are less than three elements -> return max1
#        return max3 == null ? max1 : max3;
#    }
#
#
# }


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1, max2, max3 = None, None, None
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue

            if max1 is None or num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 is None or num > max2:
                max3 = max2
                max2 = num
            elif max3 is None or num > max3:
                max3 = num

        # if there are at least three elements -> return max3
        # if there are less than three lements -> return max2
        return max1 if max3 == None else max3


