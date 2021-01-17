#Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:
#
# The left subtree values are less than the value of their parent (root) node's value.
# The right subtree values are greater than the value of their parent (root) node's value.
# Note: A subtree must include all of its descendants.
#
# Follow up: Can you figure out ways to solve it with O(n) time complexity?

#         10
#     5_         15
# 1_       8_         7

# Input: root = [10,5,15,1,8,null,7]
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.



# public class Q_0333_Largest_BST_Subtree {
#
#
#    public static void main(String[] args) {
#        Q_0333_Largest_BST_Subtree solution = new Q_0333_Largest_BST_Subtree();
#        TreeNode root = Util.buildTree("10,5,15,1,8,#,7,#,#,#,#,#,#");
#        System.out.println(solution.largestBSTSubtree(root));
#    }
#
#
#    public int largestBSTSubtree(TreeNode root) {
#        return helper(root).size;
#    }
#
#
#    private RT helper(TreeNode root) {
#        if (root == null) {
#            return new RT(Integer.MAX_VALUE, Integer.MIN_VALUE, true, 0);
#        }
#        RT left = helper(root.left);
#        RT right = helper(root.right);
#        if (left.isbst && right.isbst && root.val > left.max && root.val < right.min) {
#            return new RT(Math.min(root.val, left.min), Math.max(root.val, right.max), true, 1 + left.size + right.size);
#        } else {
#            return new RT(0, 0, false, Math.max(left.size, right.size));
#        }
#    }
#
#
#    private static class RT {
#        int min;
#        int max;
#        boolean isbst;
#        int size;
#        RT(int min, int max, boolean isbst, int size) {
#            this.min = min;
#            this.max = max;
#            this.isbst = isbst;
#            this.size = size;
#        }
#    }
# }

# similar with LC 98,, but the tree node or tupple will need an extra memeber-> no. of nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = self.helper(root)
        return result[3]

    def helper(self, root):
        # define a tuple (min subtree, max subtree, isBinaryTree, no. of nodes)
        if not root:
            return (float('inf'), float('-inf'), True, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left[2] and right[2] and root.val > left[1] and root.val < right[0]:
            return (min(left[0], root.val), max(right[1], root.val), True, left[3] + right[3] + 1)

        else:
            return (0, 0, False, max(left[3], right[3]))