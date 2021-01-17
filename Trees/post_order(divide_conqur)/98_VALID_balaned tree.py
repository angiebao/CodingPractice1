# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
#    2
#    /\
#   1  5
# Output: true


# public class Q_0098_Validate_Binary_Search_Tree {
#
#
#    public static void main(String[] args) {
#        Q_0098_Validate_Binary_Search_Tree solution = new Q_0098_Validate_Binary_Search_Tree();
#        TreeNode root1 = Util.buildTree("2,1,3,#,#,#,#");
#        TreeNode root2 = Util.buildTree("5,1,4,#,#,3,6,#,#,#,#");
#        TreeNode root3 = Util.buildTree("1,1,#,#,#");
#        System.out.println(solution.isValidBST(root1));
#        System.out.println(solution.isValidBST(root2));
#        System.out.println(solution.isValidBST(root3));
#    }
#
#
#    public boolean isValidBST(TreeNode root) {
#        return helper(root).isbst;
#    }
#
#
#    private RT helper(TreeNode root) {
#        if (root == null) {
#            return new RT(Long.MAX_VALUE, Long.MIN_VALUE, true);
#        }
#        RT left = helper(root.left);
#        RT right = helper(root.right);
#        if (left.isbst && right.isbst && root.val > left.max && root.val < right.min) {
#            return new RT(Math.min(left.min, root.val), Math.max(right.max, root.val), true);
#        } else {
#            return new RT(0, 0, false);
#        }
#    }
#
#
#    private static class RT {
#        long min;
#        long max;
#        boolean isbst;
#        RT(long min, long max, boolean isbst) {
#            this.min = min;
#            this.max = max;
#            this.isbst = isbst;
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
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        result = self.helper(root)
        return result[2]


    def helper(self, root):
        # define a tuple (min subtree, max subtree, isbinaryTree)
        if not root:
            return ( float('inf'), float('-inf') , True)

        left = self.helper(root.left)

        right = self.helper(root.right)

        if left[2] and right[2] and root.val > left[1] and root.val < right[0] :
            return (min( left[0], root.val ),  max(right[1], root.val), True )

        else:
            return (0, 0, False)


# iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        pre_num, stack = None, []
        cur = root
        # 从root出发一路向左， 找第一个node
        while cur:
            stack.append(cur)
            cur = cur.left

        while stack:
            # O（h）
            cur = stack.pop()
            if pre_num is not None and pre_num >= cur.val:
                return False
            pre_num = cur.val

            # 往右一步 再一路向左， 找下一个node
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left

        return True