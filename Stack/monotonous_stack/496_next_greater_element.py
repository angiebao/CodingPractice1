# nums 1 is subset of nums2
# return the next greater element for each eement in nums 1


# 496. Next Greater Element I
# public class Q_0496_Next_Greater_Element_I {
#
#
#    public static void main(String[] args) {
#        Q_0496_Next_Greater_Element_I solution = new Q_0496_Next_Greater_Element_I();
#        int[] nums11 = {4,1,2};
#        int[] nums21 = {1,3,4,2};
#
#
#        int[] nums12 = {2,4};
#        int[] nums22 = {1,2,3,4};
#
#
#        System.out.println(Arrays.toString(solution.nextGreaterElement(nums11, nums21)));
#        System.out.println(Arrays.toString(solution.nextGreaterElement(nums12, nums22)));
#    }
#
#
#
#
#    // 维护一个单调递减栈，遇到比栈顶小的元素入栈，遇到比栈顶大的元素开始处理
#    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
#        Map<Integer, Integer> map = new HashMap<>();
#        Deque<Integer> stack = new ArrayDeque<>();
#        for (int num : nums2) {
#            while (!stack.isEmpty() && num > stack.peekFirst()) {
#                map.put(stack.pollFirst(), num);
#            }
#            stack.offerFirst(num);
#        }
#        int[] res = new int[nums1.length];
#        for (int i = 0; i < nums1.length; i++) {
#            res[i] = map.getOrDefault(nums1[i], -1);
#        }
#        return res;
#    }
# }

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = collections.defaultdict(set)
        stack = collections.deque()
        for num in nums2:
            while stack and num > stack[-1]:
                map[stack.pop()] = num
            stack.append(num)

        res = [0 for i in range(len(nums1))]

        for i in range(len(nums1)):
            if not map[nums1[i]]:
                res[i] = -1
            else:
                res[i] = map[nums1[i]]

        return res

# my solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = collections.defaultdict(int)
        stack = []
        result1 = [-1 for i in range(len(nums1))]

        for i in range(len(nums2) - 1, -1, -1):

            cur = nums2[i]
            while stack and cur >= stack[-1]:
                stack.pop()

            if not stack:
                result[cur] = -1
            else:
                result[cur] = stack[-1]

            stack.append(cur)

        for i in range(len(nums1)):
            result1[i] = result[nums1[i]]

        return result1