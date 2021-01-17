# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# public class Q_0167_Two_Sum_II_Input_array_is_sorted {
#
#
#    public static void main(String[] args) {
#        Q_0167_Two_Sum_II_Input_array_is_sorted solution = new Q_0167_Two_Sum_II_Input_array_is_sorted();
#        int[] nums = {2,7,11,15};
#        int target = 9;
#        System.out.println(Arrays.toString(solution.twoSum(nums, target)));
#    }
#
#
#    public int[] twoSum(int[] numbers, int target) {
#        int lo = 0;
#        int hi = numbers.length-1;
#        while (lo < hi) {
#            int sum = numbers[lo] + numbers[hi];
#            if (sum == target) {
#                return new int[]{lo+1, hi+1};
#            } else if (sum < target) {
#                lo++;
#            } else {
#                hi--;
#            }
#        }
#        return new int[0];
#    }
# }

#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sums = numbers[start] + numbers[end]
            if sums == target:
                return [start + 1, end + 1]
            elif sums < target:
                start += 1
            elif sums > target:
                end -= 1

