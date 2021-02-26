# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


# public class Q_0215_Kth_Largest_Element_in_an_Array {
#
#
#    public static void main(String[] args) {
#        Q_0215_Kth_Largest_Element_in_an_Array solution = new Q_0215_Kth_Largest_Element_in_an_Array();
#        int[] nums1 = {3,2,1,5,6,4};
#        int k1 = 2;
#        int[] nums2 = {3,2,3,1,2,4,5,5,6};
#        int k2 = 4;
#        System.out.println(solution.findKthLargest1(nums1, k1));
#        System.out.println(solution.findKthLargest1(nums2, k2));
#        System.out.println(solution.findKthLargest2(nums1, k1));
#        System.out.println(solution.findKthLargest2(nums2, k2));
#    }
#
#
#    /*
#    Solution 1: Using quick select (partition)
#     */
#    public int findKthLargest1(int[] nums, int k) {
#        k = nums.length - k;
#        int lo = 0;
#        int hi = nums.length-1;
#        while (lo < hi) {
#            int pos = partition(nums, lo, hi);
#            if (pos == k) {
#                return nums[pos];
#            } else if (pos < k) {
#                lo = pos+1;
#            } else {
#                hi = pos-1;
#            }
#        }
#        return nums[lo];
#    }
#
#
#    private int partition(int[] nums, int lo, int hi) {
#        int pivot = nums[lo];
#        while (lo < hi) {
#            while (lo < hi && nums[hi] >= pivot) hi--;
#            nums[lo] = nums[hi];
#            while (lo < hi && nums[lo] <= pivot) lo++;
#            nums[hi] = nums[lo];
#        }
#        nums[lo] = pivot;
#        return lo;
#    }
#
#
#    /*
#    Solution 2: Using min heap
#     */
#    public int findKthLargest2(int[] nums, int k) {
#        Queue<Integer> pq = new PriorityQueue<>();
#        for (int num : nums) {
#            pq.offer(num);
#            if (pq.size() > k) {
#                pq.poll();
#            }
#        }
#        return pq.peek();
#    }
# }

# quick select: on average is O(N), worst case senerio, which is sorted array,
# is O(N^2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            pos = self.partition(nums, lo, hi)
            if pos == k:
                return nums[pos]
            elif pos < k:
                lo = pos + 1
            else:
                hi = pos - 1

        return nums[lo]

    def partition(self, nums, lo, hi):
        pivot = nums[lo]
        while (lo < hi):
            while lo < hi and nums[hi] >= pivot:
                hi -= 1
            nums[lo] = nums[hi]
            while lo < hi and nums[lo] <= pivot:
                lo += 1
            nums[hi] = nums[lo]

        nums[lo] = pivot
        return lo

# quick select, second  way to write

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, A, low, high, k):
        i, j = low, low
        pivot = A[high]
        while (i < high):
            if A[i] > pivot:
                self.swap(A, i, j)
                j += 1
            i += 1

        # make sure low - j elements  are larger than j+1-high elements
        self.swap(A, j, high)

        # low = j in total j+1 element
        if j + 1 == k:
            return pivot
        elif j + 1 > k:
            # find in the left
            return self.quickSelect(A, low, j - 1, k)
        else:
            # find in the right
            return self.quickSelect(A, j + 1, high, k)

    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp




