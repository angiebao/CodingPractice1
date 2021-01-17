#Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.



# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# public class Q_0230_Kth_Smallest_Element_in_a_BST {
#
#
#    public static void main(String[] args) {
#        Q_0230_Kth_Smallest_Element_in_a_BST solution = new Q_0230_Kth_Smallest_Element_in_a_BST();
#
#
#        // Solution 1:
#        TreeNode root1 = Util.buildTree("5,3,6,2,4,#,#,1,#,#,#,#,#");
#        int k1 = 3;
#        System.out.println(solution.kthSmallest1(root1, k1));
#
#
#        // Solution 2:
#        TreeNodeWithCount root2 = new TreeNodeWithCount(5);
#        solution.insert(root2, 3);
#        solution.insert(root2, 6);
#        solution.insert(root2, 2);
#        solution.insert(root2, 4);
#        solution.insert(root2, 1);
#        int k2 = 3;
#        System.out.println(solution.kthSmallest2(root2, k2));
#    }
#
#
#    // Solution 1: traditional TreeNode
#    public int kthSmallest1(TreeNode root, int k) {
#        int cnt = countNode(root.left);
#        if (cnt+1 == k) {
#            return root.val;
#        } else if (cnt+1 > k) {
#            return kthSmallest1(root.left, k);
#        } else {
#            return kthSmallest1(root.right, k-cnt-1);
#        }
#    }
#
#
#    private int countNode(TreeNode root) {
#        if (root == null) {
#            return 0;
#        }
#        return 1 + countNode(root.left) + countNode(root.right);
#    }
#
#
#    // Solution 2: augmented TreeNode
#    // https://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
#    Public int kthSmallest2(TreeNodeWithCount root, int k) {
#        int count = root.leftCount + 1;
#        if (count == k) {
#            return root.val;
#        }
#        if (count > k) {
#            return kthSmallest2(root.left, k);
#        } else {
#            return kthSmallest2(root.right, k - count);
#        }
#    }
#
#
#    public TreeNodeWithCount insert(TreeNodeWithCount root, int val) {
#        if (root == null)
#            return new TreeNodeWithCount(val);
#
#
#        if (val < root.val) {
#            root.left = insert(root.left, val);
#            root.leftCount++;
#        } else {
#            root.right = insert(root.right, val);
#        }
#        return root;
#    }
#
#
#    private static class TreeNodeWithCount {
#        int val;
#        TreeNodeWithCount left;
#        TreeNodeWithCount right;
#        int leftCount;
#        TreeNodeWithCount(int val) {
#            this.val = val;
#            leftCount = 0;
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
    # O(nlogn)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # O(n)
        cnt = self.countNode(root.left)
        if cnt + 1 == k:
            return root.val
        elif cnt + 1 > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - cnt - 1)
    # O(n)
    def countNode(self, root):
        if not root:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)

# O(n)

# Public int kthSmallest(TreeNode root, int K) {
# 	Map<TreeNode, Integer> map = new HashMap<>();
# 	countAllNodes(root, map);
# 	Return kthSmallestHelper(root, K, map);
# }
# Private int countAllNodes(TreeNode root, Map<TreeNode, Integer> map) {
# 	If (root == null) {
# 		Return 0;
# 	}
# 	Int left = countAllNodes(root.left, map);
# 	Int right = countAllNodes(root.right, map);
# 	Int numOfNodes = left + right + 1;
# 	map.put(root, numOfNodes);
# 	Return numOfNodes;
# }
# Private int kthSmallestHelper(TreeNode root, int K, Map<TreeNode, Integer> map) {
#
# 	Int numOfLeftNodes = 0;
# 	If (root.left != null) {
# 		numOfLeftNodes = map.get(root.left);
# 	}
# 	If (numOfLeftNodes >= K) {
# 		Return kthSmallestHelper(root.left, K, map);
# 	}
# 	If (numOfLeftNodes + 1 == K) {
# 		Return root.val;
# 	}
# 	Return kthSmallestHelper(root.right, K - numOfLeftNodes - 1, map);
# }

# method of O(n), use a map to store all the count

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        maps = dict()
        self.countAllNodes(root, maps)
        return self.helper(root, k, maps)

    def countAllNodes(self, root, maps):
        if root is None:
            return 0
        left = self.countAllNodes(root.left, maps)
        right = self.countAllNodes(root.right, maps)
        numOfNodes = 1 + left + right
        maps[root] = numOfNodes
        return numOfNodes

        return numOfNodes

    def helper(self, root, k, maps):
        numOfLeftNodes = 0
        if root.left:
            numOfLeftNodes = maps[root.left]
        else:
            numOfLeftNodes = 0

        if numOfLeftNodes + 1 > k:
            return self.helper(root.left, k, maps)
        elif numOfLeftNodes + 1 == k:
            return root.val
        else:
            return self.helper(root.right, k - numOfLeftNodes - 1, maps)
