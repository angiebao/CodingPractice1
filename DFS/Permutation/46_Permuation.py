# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
# ---------------------------------------------------------------

# sorted?
# numbers being positive
# duplicate numbers
# list to remove an eliement  is \
# list.remove(element)
# time complexity is O(n)
# in java, to remove a particular elemetn using treemap or tree set structure, it is log(n)

# list.pop(index)

# if to remove a parituclar index element,


# public class Q_0046_Permutations {
#
#
#    public static void main(String[] args) {
#        Q_0046_Permutations solution = new Q_0046_Permutations();
#        int[] nums1 = {1,2,3};
#        int[] nums2 = {3,2,1};
#        Util.printListOfListInteger(solution.permute(nums1));
#        Util.printListOfListInteger(solution.permute(nums2));
#    }
#
#
#    private List<List<Integer>> permute(int[] nums) {
#        List<List<Integer>> res = new ArrayList<>();
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
#                list.add(nums[i]);
#                visited[i] = true;
#                helper(nums, visited, list, res);
#                visited[i] = false;
#                list.remove(list.size() - 1);
#            }
#        }
#    }
# }

class Solution:
    def permute(self, nums):# nums: : List[int], return: List[List[int]]:
        res = []

        visited = [False for i in range(len(nums))]
        self.helper(nums, visited, [], res)
        return res

    def helper(self, nums, visited, temp, res):
        if len(temp) == len(nums):
            res.append(temp[:])
            return

        for i in range(len(nums)):
            if not visited[i]:
                temp.append(nums[i])
                visited[i] = True
                self.helper(nums, visited, temp, res)
                visited[i] = False
                temp.pop()



# how to explain:
# 1. 定义一下这个算法
# 2. break down -> 1. sort
#                  2. DFS
#                       A. remove duplicate
#                       b. when backtracking return.
#                  3.

# Cur =
# [1] -> [1,1] -> [1,1,2]
#
# Visited =
# [F,F,F] -> [T,F,F] -> [T,T,F]














# time complexity O（n!） , n factorial
#

def permutation(self, nums):
    res = []
    temp = []
    visited = [False for i in range(nums)]
    nums.sorted()
    self.helper(nums, visited, temp, res)

def helper(self, nums, visited, temp, res):

    if  len(temp) == len(nums):
        res.append(temp[:])

    itr = iter(range(len(nums)))
    for i in itr:
        if not visited[i]:
            temp.append(nums[i])
            visited[i] = True
            self.helper(nums, visited, temp, res)
            # back tracking
            visited[i] =  False
            temp.pop()
            # skip this level and start from the next number
            while i < len(nums) and nums[i] == nums[i+1]:
                next(itr)
                i+=1



