# public class Q_0106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal {
#
#
#    public static void main(String[] args) {
#        Q_0106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal solution = new Q_0106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal();
#        int[] inorder = {9,3,15,20,7};
#        int[] postorder = {9,15,7,20,3};
#        Util.printTree(solution.buildTree(inorder, postorder));
#    }
#
#
#    public TreeNode buildTree(int[] inorder, int[] postorder) {
#        Map<Integer, Integer> map = new HashMap<>();
#        for (int i = 0; i < inorder.length; i++) {
#            map.put(inorder[i], i);
#        }
#        return helper(postorder, postorder.length-1, 0, postorder.length-1, map);
#    }
#
#
#    private TreeNode helper(int[] postorder, int index, int start, int end, Map<Integer, Integer> map) {
#        if (start > end) {
#            return null;
#        }
#        int rootIndex = map.get(postorder[index]);
#        TreeNode root = new TreeNode(postorder[index]);
#        root.right = helper(postorder, index-1, rootIndex+1, end, map);
#        root.left = helper(postorder, index-(end-rootIndex)-1, start, rootIndex-1, map);
#        return root;
#    }
# }

# a second way
# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode(int x) { val = x; }
#  * }
#  */
# class Solution {
#     public TreeNode buildTree(int[] inorder, int[] postorder) {
#         if(inorder.length == 0 || postorder.length == 0){
#             return null;
#         }
#         Map<Integer, Integer> map = new HashMap<>();
#         for(int i = 0; i < inorder.length; i ++){
#             map.put(inorder[i], i);
#         }
#         return helper(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1, map);
#     }
#
#     public TreeNode helper(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd, Map<Integer, Integer> map){
#         if(inStart > inEnd || postStart > postEnd) return null;
#         TreeNode root = new TreeNode(postorder[postEnd]);
#         int index = map.get(root.val);
#         // while(index <= inEnd && inorder[index] != root.val){
#         //     index ++;
#         // }
#
#         int leftCount = index - inStart;
#
#         root.left = helper(inorder, inStart, index - 1, postorder, postStart, postStart + leftCount - 1, map);
#         root.right = helper(inorder, index + 1, inEnd, postorder, postStart + leftCount, postEnd - 1, map);
#         return root;
#     }
# }

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        map = {inorder[i]: i for i in range(len(inorder))}
        return self.helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, map)

    def helper(self, inorder, i1, i2, postorder, p1, p2, map):
        if i1 > i2 or p1 > p2:
            return None
        root = TreeNode(postorder[p2])
        index = map[root.val]

        leftCount = index - i1

        root.left = self.helper(inorder, i1, index - 1, postorder, p1, p1 + leftCount - 1, map)
        root.right = self.helper(inorder, index + 1, i2, postorder, p1 + leftCount, p2 - 1, map)
        return root