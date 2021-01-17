# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# public class Q_0257_Binary_Tree_Paths {
#
#    public static void main(String[] args) {
#        Q_0257_Binary_Tree_Paths solution = new Q_0257_Binary_Tree_Paths();
#        TreeNode root = Util.buildTree("1,2,3,#,5,#,#,#,#");
#        System.out.println(solution.binaryTreePaths1(root));
#        Util.printSeparator();
#        System.out.println(solution.binaryTreePaths2(root));
#    }
#
#    /*
#        Solution 1: use pre-order traversal
#     */
#    public List<String> binaryTreePaths1(TreeNode root) {
#        List<String> res = new ArrayList<>();
#        helper1(root, new StringBuilder(), res);
#        return res;
#    }
#
#    private void helper1(TreeNode root, StringBuilder sb, List<String> res) {
#        if (root == null) {
#            return;
#        }
#        int len = sb.length();
#        if (sb.length() > 0) {
#            sb.append("->");
#        }
#        sb.append(root.val);
#        if (root.left == null && root.right == null) {
#            res.add(sb.toString());
#        } else {
#            helper1(root.left, sb, res);
#            helper1(root.right, sb, res);
#        }
#        sb.setLength(len);
#    }
#
#    /*
#       Solution 2: 分治法
#    */
#    public List<String> binaryTreePaths2(TreeNode root) {
#        List<String> paths = new ArrayList<>();
#        if (root == null) {
#            return paths;
#        }
#        List<String> left = binaryTreePaths2(root.left);
#        List<String> right = binaryTreePaths2(root.right);
#
#        for (String path : left) {
#            paths.add(root.val + "->" + path);
#        }
#        for (String path : right) {
#            paths.add(root.val + "->" + path);
#        }
#
#        if (paths.size() == 0) {
#            paths.add("" + root.val);
#        }
#        return paths;
#    }
# }

# post order
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if root is None:
            return paths

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        for path in left:
            paths.append(str(root.val) + "->" + path)

        for path in right:
            paths.append(str(root.val) + '->' + path)

        if len(paths) == 0:
            paths.append("" + str(root.val))

        return paths

# pre order
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        temp = ""
        self.helper(root, temp, res)
        return res

    def helper(self, root, temp, res):
        if not root:
            return

        if (not root.left) and (not root.right):
            temp += str(root.val)
            res.append(temp)
            return

        temp += str(root.val)
        self.helper(root.left, temp + '->', res)
        self.helper(root.right, temp + '->', res)



