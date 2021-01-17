#Given an integer array nums, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]

# public class Q_0078_Subsets {
#
#
#    public static void main(String[] args) {
#        Q_0078_Subsets solution = new Q_0078_Subsets();
#        int[] nums = {1,2,3};
#        System.out.println(solution.subsets(nums));
#    }
#
#
#    public List<List<Integer>> subsets(int[] nums) {
#        List<List<Integer>> res = new ArrayList<>();
#        helper(nums, 0, new ArrayList<>(), res);
#        return res;
#    }
#
#
#    private void helper(int[] A, int start, List<Integer> list, List<List<Integer>> res) {
#        res.add(new ArrayList<>(list));
#        for (int i = start; i < A.length; i++) {
#            list.add(A[i]);
#            helper(A, i+1, list, res);
#            list.remove(list.size()-1);
#        }
#    }
# }


#穷举的思想，也就是，放进subset or 不放进subset，类似combination,是满二叉树，
# time complexity is N* 2^N ， but larger than the second method
# Space same

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        self.helper(nums, start, temp, res)
        return res

    def helper(self, nums, start, temp, res):
        res.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.helper(nums, i + 1, temp, res)
            temp.pop()

# 不是满二叉树，time complexity is N*2^N
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        start = 0
        self.helper(nums, start, temp, res)
        return res

    def helper(self, nums, start, temp, res):
        res.append(temp[:])

        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.helper(nums, i + 1, temp, res)
            temp.pop()

# duplicate numbers/or use multiple times
# sort or not, sort can help reduce time complexity, for example,
# does permuation in the result list count as a different result.


[1, 2, 3]
Res = [[1], [1,2], [1,2,2] ]
Temp = [1, 2, 2], [1,2]  ,
Start = 0, 1, 2,   1,

start = 0,  1, 2
temp =  [1], [1,2], [1,2,2] ,

start = 1


start = 2


