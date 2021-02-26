# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.


# public class Q_0347_Top_K_Frequent_Elements {
#
#
#    public static void main(String[] args) {
#        Q_0347_Top_K_Frequent_Elements solution = new Q_0347_Top_K_Frequent_Elements();
#        int[] nums1 = {1,1,1,2,2,3};
#        int k1 = 2;
#        int[] nums2 = {1};
#        int k2 = 1;
#        System.out.println(Arrays.toString(solution.topKFrequent1(nums1, k1)));
#        System.out.println(Arrays.toString(solution.topKFrequent1(nums2, k2)));
#        System.out.println(Arrays.toString(solution.topKFrequent2(nums1, k1)));
#        System.out.println(Arrays.toString(solution.topKFrequent2(nums2, k2)));
#    }
#
#
#    /*
#    Solution 1: bucket sort
#     */
#    public int[] topKFrequent1(int[] nums, int k) {
#        List<Integer>[] buckets = new List[nums.length+1];
#        Map<Integer, Integer> map = new HashMap<>();
#        for (int num : nums) {
#            map.put(num, map.getOrDefault(num, 0) + 1);
#        }
#        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
#            int cnt = entry.getValue();
#            if (buckets[cnt] == null) {
#                buckets[cnt] = new ArrayList<>();
#            }
#            buckets[cnt].add(entry.getKey());
#        }
#
#
#        List<Integer> res = new ArrayList<>();
#        // insert higher frequency element to the result first
#        for (int i = buckets.length-1; i >= 1; i--) {
#            if (buckets[i] == null) {
#                continue;
#            }
#            res.addAll(buckets[i]);
#            if (res.size() >= k) {
#                break;
#            }
#        }
#        return res.subList(0, k).stream().mapToInt(i -> i).toArray();
#    }
#
#
#    /*
#    Solution 2: heap
#     */
#    public int[] topKFrequent2(int[] nums, int k) {
#        Map<Integer, Integer> map = new HashMap<>();
#        for (int num : nums) {
#            map.put(num, map.getOrDefault(num, 0) + 1);
#        }
#        // 建立最小堆
#        Comparator<Integer> comparator = (a, b) -> map.get(a) - map.get(b);
#        Queue<Integer> pq = new PriorityQueue<>(comparator);
#        for (int num : map.keySet()) {
#            pq.offer(num);
#            if (pq.size() > k) {
#                pq.poll();
#            }
#        }
#        // 此时最小堆有k个元素
#        int[] res = new int[k];
#        for (int i = 0; i < k; i++) {
#            res[i] = pq.poll();
#        }
#        return res;
#    }
# }

# heap sort, O(n), if use heapsort, it is nlogK
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # butket sort
        buckets = [[] for i in range(len(nums) + 1)]
        maps = defaultdict(int)
        for num in nums:
            maps[num] += 1

        for key, value in maps.items():
            cnt = value
            if len(buckets[cnt]) == 0:
                buckets[cnt] = []

            buckets[cnt].append(key)

        res = []
        # insert higher frequency element to the result first
        for i in range(len(buckets) - 1, 0, -1):

            if len(buckets[i]) == 0:
                continue
            res.extend(buckets[i])
            if len(res) >= k:
                break

        return res