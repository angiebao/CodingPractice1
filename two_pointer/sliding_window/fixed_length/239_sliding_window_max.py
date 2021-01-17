# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Example 3:
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:
#
# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length



# de = collections.deque()
# de.append()
# de.appendleft()
# de.pop()
# de.popleft()
# de[-1]

# public class Q_0239_Sliding_Window_Maximum {
#
#
#    public static void main(String[] args) {
#        Q_0239_Sliding_Window_Maximum solution = new Q_0239_Sliding_Window_Maximum();
#        int[] nums = {1,3,-1,-3,5,3,6,7};
#        int k = 3;
#        System.out.println(Arrays.toString(solution.maxSlidingWindow1(nums, k)));
#        System.out.println(Arrays.toString(solution.maxSlidingWindow2(nums, k)));
#    }
#
#
#    // Solution 1: using deque
#    public int[] maxSlidingWindow1(int[] nums, int k) {
#        Deque<Integer> deque = new ArrayDeque<>();
#        int[] res = new int[nums.length-k+1];
#        for (int i = 0; i < nums.length; i++) {
#            while (!deque.isEmpty() && nums[i] > deque.peekLast());
#            deque.offerLast(nums[i]); //append
#            if (i >= k-1) {
#                res[i-k+1] = deque.peekFirst();
#                if (nums[i-k+1] == deque.peekFirst()) deque.pollFirst(); //pop
#            }‚
#        }
#        return res;
#    }
import collections

def maxSlidingWindow(self, nums, k):
    de = collections.deque()
    n = len(nums)
    res = [0 for i in range(n - k + 1)]
    for i in range(n):
        # pop out the right element that will not be the max values. Leave only the values co
        while de and nums[i] > de[-1]:
            de.pop()
        de.append(nums[i])
        if i >= k-1:
            res[i-k+1] = de[0]
            # pop out the left element if it will be moved out side sliding window
            if nums[i-k+1] == de[0]:
                de.popleft()
    return res


#
#    // Solution 2: using heap
#    public int[] maxSlidingWindow2(int[] nums, int k) {
#        Comparator<Integer> comparator = (i, j) -> nums[i] != nums[j] ? nums[i] - nums[j] : i - j;
#        TreeSet<Integer> maxSet = new TreeSet<>(comparator.reversed());
#        int[] res = new int[nums.length-k+1];
#        for (int i = 0; i < nums.length; i++) {
#            maxSet.add(i);
#            if (i >= k-1) {
#                res[i-k+1] = nums[maxSet.first()];
#                maxSet.remove(i-k+1);
#            }
#        }
#        return res;
#    }
# }

