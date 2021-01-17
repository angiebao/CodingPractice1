# prefix sum and 单调 stack
# less time , more space

# inclusive or exclusive

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
#
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#


# public class Q_0303_Range_Sum_Query_Immutable {
#
#
#    public static void main(String[] args) {
#        int[] nums = {-2, 0, 3, -5, 2, -1};
#        NumArray numArray = new NumArray(nums);
#        System.out.println(numArray.sumRange(0, 2));
#        System.out.println(numArray.sumRange(2, 5));
#        System.out.println(numArray.sumRange(0, 5));
#    }
#
#
#    static class NumArray {
#
#
#        private int[] sum;
#
#
#        public NumArray(int[] nums) {
#            sum = new int[nums.length+1];
#            sum[0] = 0;
#            for (int i = 1; i <= nums.length; i++) {
#                sum[i] = sum[i-1] + nums[i-1];
#            }
#        }
#
#
#        public int sumRange(int i, int j) {
#            return sum[j+1] - sum[i];
#        }
#    }
#
#
# }

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0 for i in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)