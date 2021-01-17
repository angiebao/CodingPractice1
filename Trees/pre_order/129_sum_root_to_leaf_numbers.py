#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # put all root to leaf numbers in array
        if root == None:
            return 0

        self.result = []
        self.path = []
        self.dfs(root)

        totalSum = 0
        for items in self.result:
            sums = 0
            for item in items:
                sums = sums * 10 + item

            totalSum += sums

        return totalSum

    def dfs(self, root):

        if root.left == None and root.right == None:
            self.path.append(root.val)
            self.result.append(self.path[:])
            self.path.pop()  # leaf
            return

        self.path.append(root.val)

        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

        self.path.pop()  # root


#
# public class Q_0129_Sum_Root_to_Leaf_Numbers {
#
#
#    public static void main(String[] args) {
#        Q_0129_Sum_Root_to_Leaf_Numbers solution = new Q_0129_Sum_Root_to_Leaf_Numbers();
#        TreeNode root1 = Util.buildTree("1,2,3,#,#,#,#");
#        TreeNode root2 = Util.buildTree("4,9,0,5,1,#,#,#,#,#,#");
#        TreeNode root3 = Util.buildTree("0,1,#,#,#");
#        System.out.println(solution.sumNumbers(root1));
#        System.out.println(solution.sumNumbers(root2));
#        System.out.println(solution.sumNumbers(root3));
#    }
#
#
#    public int sumNumbers(TreeNode root) {
#        return helper(root, 0);
#    }
#
#
#    private int helper(TreeNode root, int curSum) {
#        if (root == null) {
#            return 0;
#        }
#        curSum = 10 * curSum + root.val;
#        if (root.left == null && root.right == null) {
#            return curSum;
#        }
#        int left = helper(root.left, curSum);
#        int right = helper(root.right, curSum);
#        return left + right;
#    }
# }
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        result = self.helper(root, 0)
        return result

    def helper(self, root, curSum):
        # suitable for node have only one child
        if not root:
            return 0
        # top down add, pre order, calculate the root first
        curSum = 10 * curSum + root.val
        if root.left is None and root.right is None:
            return curSum

        left = self.helper(root.left, curSum)
        right = self.helper(root.right, curSum)
        # this part is to
        return left + right



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root, 0)

    def helper(self, root, curSum):
        if not root:
            return 0
        curSum = 10 * curSum + root.val
        if root.left is None and root.right is None:
            return curSum

        left = self.helper(root.left, curSum)
        right = self.helper(root.right, curSum)
        return left + right