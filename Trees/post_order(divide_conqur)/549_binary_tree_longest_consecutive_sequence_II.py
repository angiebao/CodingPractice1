# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
#
# Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
#
# Example 1:
#
# Input:
#         1
#        / \
#       2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
#
#
# Example 2:
#
# Input:
#         2
#        / \
#       1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#
#
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].


# public class Q_0549_Binary_Tree_Longest_Consecutive_Sequence_II {
#
#
#    public static void main(String[] args) {
#        Q_0549_Binary_Tree_Longest_Consecutive_Sequence_II solution = new Q_0549_Binary_Tree_Longest_Consecutive_Sequence_II();
#        TreeNode root1 = Util.buildTree("1,2,3,#,#,#,#");
#        TreeNode root2 = Util.buildTree("2,1,3,#,#,#,#");
#        System.out.println(solution.longestConsecutive(root1));
#        System.out.println(solution.longestConsecutive(root2));
#    }
#
#
#    public int longestConsecutive(TreeNode root) {
#        return helper(root).max;
#    }
#
#
#    private RT helper(TreeNode root) {
#        if (root == null) {
#            return new RT(0, 0, 0);
#        }
#        RT left = helper(root.left);
#        RT right = helper(root.right);
#        int inc = 1;
#        int dec = 1;
#        if (root.left != null) {
#            if (root.val + 1 == root.left.val) {
#                inc = Math.max(inc, left.inc + 1);
#            } else if (root.val - 1 == root.left.val) {
#                dec = Math.max(dec, left.dec + 1);
#            }
#        }
#        if (root.right != null) {
#            if (root.val + 1 == root.right.val) {
#                inc = Math.max(inc, right.inc + 1);
#            } else if (root.val - 1 == root.right.val) {
#                dec = Math.max(dec, right.dec + 1);
#            }
#        }
#        int max = Math.max(inc+dec-1, Math.max(left.max, right.max));
#        return new RT(inc, dec, max);
#    }
#
#
#    private static class RT {
#        int inc;
#        int dec;
#        int max;
#        RT(int inc, int dec, int max) {
#            this.inc = inc;
#            this.dec = dec;
#            this.max = max;
#        }
#    }
# }

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        # define a tuple (inc, dec, max )
        return self.helper(root)[2]

    def helper(self, root):
        if root is None:
            return (0, 0, 0)
        left = self.helper(root.left)
        right = self.helper(root.right)

        inc = 1
        dec = 1

        if root.left:
            if root.val + 1 == root.left.val:
                inc = max(inc, left[0] + 1)
            elif root.val - 1 == root.left.val:
                dec = max(dec, left[1] + 1)

        if root.right:
            if root.val + 1 == root.right.val:
                inc = max(inc, right[0] + 1)
            elif root.val - 1 == root.right.val:
                dec = max(dec, right[1] + 1)

        maxvalue = max(inc + dec - 1, max(left[2], right[2]))

        return (inc, dec, maxvalue)




