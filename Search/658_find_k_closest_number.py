# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
# Example 1:
#
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
#
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]



# 658. Find K Closest Elements
# public class Q_0658_Find_K_Closest_Elements {
#
#
#    public static void main(String[] args) {
#        Q_0658_Find_K_Closest_Elements solution = new Q_0658_Find_K_Closest_Elements();
#        int[] nums1 = {1,2,3,4,5};
#        int k1 = 4;
#        int x1 = 3;
#        int x2 = -1;
#        System.out.println(solution.findClosestElements(nums1, k1, x1));
#        System.out.println(solution.findClosestElements(nums1, k1, x2));
#
#
#        int[] nums2 = {0,0,1,2,3,3,4,7,7,8};
#        int k2 = 3;
#        int x3 = 5;
#        System.out.println(solution.findClosestElements(nums2, k2, x3));
#    }
#
#
#    // https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
#
#
#    /*
#    case 1: x - A[mid] < A[mid + k] - x, need to move window go left
#    -------x----A[mid]-----------------A[mid + k]----------
#
#
#    case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
#    -------A[mid]----x-----------------A[mid + k]----------
#
#
#    case 3: x - A[mid] > A[mid + k] - x, need to move window go right
#    -------A[mid]------------------x---A[mid + k]----------
#
#
#    case 4: x - A[mid] > A[mid + k] - x, need to move window go right
#    -------A[mid]---------------------A[mid + k]----x------
#     */
#
#
#    /*
#    Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
#    It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3
#
#
#    => we cannot tell the solution is on the left or right part when abs(x - A[mid]) == abs(A[mid + k] - x)
#     */
#
#
#    public List<Integer> findClosestElements(int[] arr, int k, int x) {
#        int lo = 0;
#        int hi = arr.length-k;
#        while (lo+1<hi) {
#            int mid = lo+(hi-lo)/2;
#            if (x - arr[mid] <= arr[mid+k] - x) {
#                hi = mid;
#            } else {
#                lo = mid;
#            }
#        }
#
#
#        // compare result of "lo" and "hi"
#        int idx = getDiff(arr, k, x, lo) <= getDiff(arr, k, x, hi) ? lo : hi;
#        return Arrays.stream(arr, idx, idx + k).boxed().collect(Collectors.toList());
#    }
#
#
#    private int getDiff(int[] A, int k, int x, int start) {
#        int diff = 0;
#        for (int i = start; i < start+k; i++) {
#            diff += Math.abs(A[i] - x);
#        }
#        return diff;
#    }
# }

# find >= x left most
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left lower bound: >=x left most
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid
        index2 = len(arr)
        if arr[left] >= x:
            index2 = left
        elif arr[right] >= x:
            index2 = right

        # arr[index2] >=x left most
        # arr[index2-1]<x right most

        # 1 2 2 2 3 target2
        # 0 0 1 1 1 1 1#
        index1 = index2 - 1
        ans = []
        while len(ans) < k:
            if index2 == len(arr) or (index1 >= 0 and x - arr[index1] <= arr[index2] - x):
                ans.append(arr[index1])
                index1 -= 1
            else:
                ans.append(arr[index2])
                index2 += 1
        return sorted(ans)


# find < x right most

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find < x right most
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid

        index1 = -1
        if arr[right] < x:
            index1 = right
        elif arr[left] < x:
            index1 = left

        # arr[index2] >=x left most
        # arr[index2-1]<x right most

        # 1 2 2 2 3 target2
        # 0 0 1 1 1 1 1#
        index2 = index1 + 1
        ans = []
        while len(ans) < k:
            if index2 == len(arr) or (index1 >= 0 and x - arr[index1] <= arr[index2] - x):
                ans.append(arr[index1])
                index1 -= 1
            else:
                ans.append(arr[index2])
                index2 += 1
        return sorted(ans)


# find <=x right most

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find <= x right most
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            mid = (right + left) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid

        index1 = -1
        if arr[right] <= x:
            index1 = right
        elif arr[left] <= x:
            index1 = left

        # arr[index2] >=x left most
        # arr[index2-1]<x right most

        # 1 2 2 2 3 target2
        # 0 0 1 1 1 1 1#
        index2 = index1 + 1
        ans = []
        while len(ans) < k:
            if index2 == len(arr) or (index1 >= 0 and x - arr[index1] <= arr[index2] - x):
                ans.append(arr[index1])
                index1 -= 1
            else:
                ans.append(arr[index2])
                index2 += 1
        return sorted(ans)






