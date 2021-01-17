# input nums[5,7,7,8,8,10] target 8
# output [3,4]
# if target = 6 return [-1, -1]
# find the starting and ending position of a given target value


# public class Q_0034_Find_First_and_Last_Position_of_Element_in_Sorted_Array {
#
#    public static void main(String[] args) {
#        Q_0034_Find_First_and_Last_Position_of_Element_in_Sorted_Array solution = new Q_0034_Find_First_and_Last_Position_of_Element_in_Sorted_Array();
#        int[] nums = {5,7,7,8,8,10};
#        int target1 = 8;
#        int target2 = 6;
#
#        System.out.println(Arrays.toString(solution.searchRange(nums, target1)));
#        System.out.println(Arrays.toString(solution.searchRange(nums, target2)));
#    }
#
#    public int[] searchRange(int[] nums, int target) {
#        int[] res = new int[]{-1, -1};
#        if (nums.length == 0) {
#            return res;
#        }
#        int lb = bs(nums, target, true);
#        if (lb != -1) {
#            int ub = bs(nums, target, false);
#            res[0] = lb;
#            res[1] = ub;
#        }
#        return res;
#    }
#
#    private int bs(int[] nums, int target, boolean lower) {
#        int lo = 0;
#        int hi = nums.length-1;
#        while (lo + 1 < hi) {
#            int mid = lo + (hi-lo)/2;
#            if (lower) {
#                if (nums[mid] < target) {
#                    lo = mid;
#                } else {
#                    hi = mid;
#                }
#            } else {
#                if (nums[mid] <= target) {
#                    lo = mid;
#                } else {
#                    hi = mid;
#                }
#            }
#        }
#
#        if (lower) {
#            if (target == nums[lo]) {
#                return lo;
#            } else if (target == nums[hi]) {
#                return hi;
#            }
#        } else {
#            if (target == nums[hi]) {
#                return hi;
#            } else if (target == nums[lo]) {
#                return lo;
#            }
#        }
#        return -1;
#    }
# }
import math

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1

        while left + 1 < right:  # ensure no infinite loop
            mid = left + math.floor((right - left) / 2)
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                right = mid

        if nums[left] == target:
            first = left
        elif nums[right] == target:
            first = right
        else:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        while left + 1 < right:  # ensure no infinite loop
            mid = left + math.floor((right - left) / 2)
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            last = right
        elif nums[left] == target:
            last = left
        else:
            return [-1, -1]

        return [first, last]


