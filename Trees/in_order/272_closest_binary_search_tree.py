# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: [4,3]
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# public class Q_0272_Closest_Binary_Search_Tree_Value_II {
#
#
#    public static void main(String[] args) {
#        Q_0272_Closest_Binary_Search_Tree_Value_II solution = new Q_0272_Closest_Binary_Search_Tree_Value_II();
#        TreeNode root = Util.buildTree("4,2,5,1,3,#,#,#,#,#,#");
#        double target = 3.714286;
#        int k = 2;
#        System.out.println(solution.closestKValues(root, target, k));
#    }
#
#
#    // Clarification:
#    // 1. You may assume k is always valid, that is: k ≤ total nodes.
#    // 2. You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
#    public List<Integer> closestKValues(TreeNode root, double target, int k) {
#        LinkedList<Integer> res = new LinkedList<>();
#        inorder(root, target, k, res);
#        return res;
#    }
#
#
#    private void inorder(TreeNode root, double target, int k, LinkedList<Integer> res) {
#        if (root == null) {
#            return;
#        }
#        inorder(root.left, target, k, res);
#        if (res.size() == k) {
#            int first = res.getFirst();
#            if (Math.abs(root.val - target) < Math.abs(first - target)) {
#                res.pollFirst();
#            } else {
#                return;
#            }
#        }
#        res.add(root.val);
#        inorder(root.right, target, k, res);
#    }
#
#
# }

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = collections.deque()
        self.inorder(root, target, k, res)

        return res

    def inorder(self, root, target, k, res):
        if not root:
            return
        self.inorder(root.left, target, k, res)
        if len(res) == k:
            first = res[0]
            if abs(root.val - target) < abs(first - target):
                res.popleft()
            else:
                return

        res.append(root.val)
        self.inorder(root.right, target, k, res)

