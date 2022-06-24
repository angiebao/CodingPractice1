# # list might contains duplicates
# 47.
# Permutations
# II
# Medium
#
# Given a collection of numbers, nums, that might contain duplicates, return all possible
# unique permutations in any order.
#
# Example
# 1:
#
# Input: nums = [1, 1, 2]
# Output:
# [[1, 1, 2],
#  [1, 2, 1],
#  [2, 1, 1]]
# Example
# 2:
#
# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
#
# Constraints:
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#


# public class Q_0047_Permutations_II {
#
#
#    public static void main(String[] args) {
#        Q_0047_Permutations_II solution = new Q_0047_Permutations_II();
#        int[] nums = {1,1,2};
#        System.out.println(solution.permuteUnique(nums));
#    }
#
#
#    public List<List<Integer>> permuteUnique(int[] nums) {
#        List<List<Integer>> res = new ArrayList<>();
#        Arrays.sort(nums);
#        helper(nums, new boolean[nums.length], new ArrayList<>(), res);
#        return res;
#    }
#
#
#    private void helper(int[] nums, boolean[] visited, List<Integer> list, List<List<Integer>> res) {
#        if (list.size() == nums.length) {
#            res.add(new ArrayList<>(list));
#            return;
#        }
#        for (int i = 0; i < nums.length; i++) {
#            if (!visited[i]) {
#                visited[i] = true;
#                list.add(nums[i]);
#                helper(nums, visited, list, res);
#                list.remove(list.size()-1);
#                visited[i] = false;
#
#
#                while (i+1 < nums.length && nums[i] == nums[i+1]) i++;
#            }
#        }
#    }
# }

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return []
#         nums.sort()
#         res = list()
#         temp = list()
#         is_visited = [False for _ in range(len(nums))]
#         self.dfs(res, temp, is_visited, nums)
#         return res
#
#     def dfs(self, res, temp, is_visited, nums):
#         if len(temp) == len(nums):
#             res.append(temp[:])
#             return
#
#         for i in range(len(nums)):
#             if is_visited[i]:
#                 continue
#             if i > 0 and nums[i] == nums[i - 1] and is_visited[i - 1] == 0:
#                 continue
#             temp.append(nums[i])
#             is_visited[i] = True
#             self.dfs(res, temp, is_visited, nums)
#             is_visited[i] = False
#             temp.pop()

#another way of writing this :
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [False for i in range(len(nums))]
        self.helper(nums, visited, [], res)

        return res

    def helper(self, nums, visited, temp, res):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        itr = iter(range(len(nums)))
        for i in itr:
            if not visited[i]:
                visited[i] = True
                temp.append(nums[i])
                self.helper(nums, visited, temp, res)
                temp.pop()
                visited[i] = False
                # e.g.first level dfs finished,
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                    next(itr)

# itr = iter(range(10))
# for i in itr:
#     if i == 1:
#         # the following two lines combined will skip iteration at i==1
#         i+=1
#         next(itr)
#     print(i)
