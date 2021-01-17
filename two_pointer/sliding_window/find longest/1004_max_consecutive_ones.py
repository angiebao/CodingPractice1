
# public class Q_1004_Max_Consecutive_Ones_III {
#
#
#    public static void main(String[] args) {
#        Q_1004_Max_Consecutive_Ones_III solution = new Q_1004_Max_Consecutive_Ones_III();
#        int[] A1 = {1,1,1,0,0,0,1,1,1,1,0};
#        int K1 = 2;
#        int[] A2 = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
#        int K2 = 3;
#        System.out.println(solution.longestOnes(A1, K1));
#        System.out.println(solution.longestOnes(A2, K2));
#    }
#
#
#    public int longestOnes(int[] A, int K) {
#        int start = 0;
#        int end = 0;
#        int res = 0;
#        int cnt = 0;
#        while (start < A.length) {
#            while (end < A.length) {
#                if (A[end] == 0) {
#                    cnt++;
#                }
#                end++;
#                if (cnt <= K) {
#                    res = Math.max(res, end-start);
#                } else {
#                    break;
#                }
#            }
#            if (A[start] == 0) {
#                cnt--;
#            }
#            start++;
#        }
#        return res;
#    }
# }

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        end = 0
        res = 0
        cnt = 0
        while start < len(A):
            while end<len(A):
                if A[end] == 0:
                    cnt += 1
                end += 1
                if cnt <= K:
                    res = max(res, end - start)
                else:
                    break

            if A[start] == 0:
                cnt -= 1
            start += 1
        return res
