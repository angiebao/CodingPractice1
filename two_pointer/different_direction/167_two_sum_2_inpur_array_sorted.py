class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two sums I: O(n) time, space(O(n))
        # two sums II: O(n) time, space O(1)
        # 从两边逼近
        low = 0
        high = len(numbers) - 1

        while low < high:

            if numbers[low] + numbers[high] > target:
                if numbers[low] > numbers[high]:
                    low += 1
                else:
                    high -= 1
            elif numbers[low] + numbers[high] < target:
                if numbers[low] < numbers[high]:
                    low += 1
                else:
                    high -= 1
            else:
                return [low + 1, high + 1]




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

def twosum(self,nums, target):
    low = 0
    high =  len(nums)
    while low< high:
        sums = nums[low] + nums[high]
        if sum == target:
            return True
        elif sums< target:
            low +=1
        else :
            high -=1

    return False