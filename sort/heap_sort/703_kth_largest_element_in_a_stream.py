# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Implement KthLargest class:
#
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Returns the element representing the kth largest element in the stream.
#
#
# Example 1:
#
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
#
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#
#
# Constraints:
#
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.



# heap: online: O(k)
#       offline: O(N) + O(Nlogk), O(N) to build the heap, and O(NlogK) to sort




# public class Q_0703_Kth_Largest_Element_in_a_Stream {
#
#
#    public static void main(String[] args) {
#        KthLargest kthLargest1 = new KthLargest(3, new int[]{4,5,8,2});
#        System.out.println(kthLargest1.add(3));
#        System.out.println(kthLargest1.add(5));
#        System.out.println(kthLargest1.add(10));
#        System.out.println(kthLargest1.add(9));
#        System.out.println(kthLargest1.add(4));
#
#
#        Util.printSeparator();
#
#
#        KthLargest kthLargest2 = new KthLargest(1, new int[0]);
#        System.out.println(kthLargest2.add(-3));
#        System.out.println(kthLargest2.add(-2));
#        System.out.println(kthLargest2.add(-4));
#        System.out.println(kthLargest2.add(0));
#        System.out.println(kthLargest2.add(4));
#    }
#
#
#    static class KthLargest {
#
#
#        private Queue<Integer> pq;
#        private int k;
#
#
#        public KthLargest(int k, int[] nums) {
#            this.k = k;
#            pq = new PriorityQueue<>();
#            for (int num : nums) {
#                pq.offer(num);
#                if (pq.size() > k) {
#                    pq.poll();
#                }
#            }
#        }
#
#
#        public int add(int val) {
#            pq.offer(val);
#            if (pq.size() > k) {
#                pq.poll();
#            }
#            return pq.peek();
#        }
#    }
# }
