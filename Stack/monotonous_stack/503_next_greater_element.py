# 503. Next Greater Element II
# public class Q_0503_Next_Greater_Element_II {
#
#
#    public static void main(String[] args) {
#        Q_0503_Next_Greater_Element_II solution = new Q_0503_Next_Greater_Element_II();
#        int[] nums = {1,2,1};
#        System.out.println(Arrays.toString(solution.nextGreaterElements(nums)));
#    }
#
#
#    // 维护一个单调递减栈
#    // traverse the array twice
#    // 栈中存放的是index
#    public int[] nextGreaterElements(int[] nums) {
#        int n = nums.length;
#        int[] res = new int[n];
#        Arrays.fill(res, -1);
#        Deque<Integer> stack = new ArrayDeque<>();
#        for (int i = 0; i < 2*n; i++) {
#            int val = nums[i%n];
#            while (!stack.isEmpty() && val > nums[stack.peekFirst()]) {
#                res[stack.pollFirst()] = val;
#            }
#            if (i < n) {
#                stack.offerFirst(i);
#            }
#        }
#        return res;
#    }
# }

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # put a copy of nums after nums, becuase we only need to loop at most two times through nums

        nums_copy = nums + nums
        # use the stack to store the max value so far, if we met a value larger than the value at the top of the stack, we remove the top of element at the top of the stack until the current met value is smaller, if this result in an empty stack, then the result will be -1 for the current element
        stack = []
        result = [0 for i in range(len(nums_copy))]

        for i in range(len(nums_copy) - 1, -1, -1):
            cur = nums_copy[i]

            while stack and cur >= stack[-1]:
                stack.pop()

            if (not stack):
                result[i] = -1
            else:
                result[i] = stack[-1]

            stack.append(cur)

        return result[:len(nums)]


# isntructor's soutlion
