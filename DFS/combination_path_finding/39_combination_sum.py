# Given an array of [distinct] integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to target is less than
# 150 combinations for the given input.
#
#
#
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
# Example 4:
#
# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:
#
# Input: candidates = [1], target = 2
# Output: [[1,1]]
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500



# public class Q_0039_Combination_Sum {
#
#
#    public static void main(String[] args) {
#        Q_0039_Combination_Sum solution = new Q_0039_Combination_Sum();
#        int[] candidates1 = {2,3,6,7};
#        int target1 = 7;
#        int[] candidates2 = {2,3,5};
#        int target2 = 8;
#        System.out.println(solution.combinationSum(candidates1, target1));
#        System.out.println(solution.combinationSum(candidates2, target2));
#    }
#
#
#    public List<List<Integer>> combinationSum(int[] candidates, int target) {
#        List<List<Integer>> res = new ArrayList<>();
#        helper(candidates, target, 0, 0, new ArrayList<>(), res);
#        return res;
#    }
#
#
#    private void helper(int[] A, int target, int start, int sum, List<Integer> list, List<List<Integer>> res) {
#        if (sum > target) {
#            return;
#        }
#        if (sum == target) {
#            res.add(new ArrayList<>(list));
#            return;
#        }
#        for (int i = start; i < A.length; i++) {
#            list.add(A[i]);
#            helper(A, target, i, sum + A[i], list, res);
#            list.remove(list.size() - 1);
#        }
#    }

from collections import Counter, defaultdict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # candidates.sort()
        self.helper(candidates, target, 0, 0, [], res)
        return res

    def helper(self, candidates, target, start, sumValue, temp, res):
        if sumValue > target:
            return
        if sumValue == target:
            res.append(temp[:])
            return

        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            # can repeatedly use one number, so the start is the i , not i + 1
            self.helper(candidates, target, i, sumValue + candidates[i], temp, res)
            temp.pop()

# can use once or multiple times
# sort or not, sort can help reduce time complextity, for example,
# if the sum already exceeded target, the rest elemet does not need to try out?

# sort version:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        start = 0
        candidates.sort()
        # does not need visited because each word can be used multiple times.
        self.dfs(start, curr, res, target, candidates)
        return res

    def dfs(self, start, curr, res, target, candidates):

        if sum(curr) == target:
            res.append(curr[:])

        for i in range(start, len(candidates)):
            if sum(curr) + candidates[i] > target:
                return
            curr.append(candidates[i])
            self.dfs(i, curr, res, target, candidates)
            curr.pop()

