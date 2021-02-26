# first way
# public class Q_0105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal {
#
#
#    public static void main(String[] args) {
#        Q_0105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal solution = new Q_0105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal();
#        int[] preorder = {3,9,20,15,7};
#        int[] inorder = {9,3,15,20,7};
#        Util.printTree(solution.buildTree(preorder, inorder));
#    }
#
#
#    public TreeNode buildTree(int[] preorder, int[] inorder) {
#        Map<Integer, Integer> map = new HashMap<>();
#        for (int i = 0; i < inorder.length; i++) {
#            map.put(inorder[i], i);
#        }
#        return helper(preorder, 0, 0, preorder.length-1, map);
#    }
#
#
#    private TreeNode helper(int[] preorder, int index, int start, int end, Map<Integer, Integer> map) {
#        if (start > end) {
#            return null;
#        }
#        int rootIndex = map.get(preorder[index]);
#        TreeNode root = new TreeNode(preorder[index]);
#        root.left = helper(preorder, index+1, start, rootIndex-1, map);
#        root.right = helper(preorder, index+(rootIndex-start)+1, rootIndex+1, end, map);
#        return root;
#    }
# }

# second way
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
#
#     def build(self, preorder, i1, j1, inorder, i2, j2):
#         if i1 > j1:
#             return None
#         if i1 == j1:
#             return TreeNode(preorder[i1])
#         root_val = preorder[i1]
#         index = i2
#         while inorder[index] != root_val:
#             index += 1
#         left_size, right_size = index - i2, j2 - index
#         root = TreeNode(root_val)
#         root.left = self.build(preorder, i1 + 1, i1 + left_size, inorder, i2, index - 1)
#         root.right = self.build(preorder, i1 + left_size + 1, j1, inorder, index + 1, j2)
#         return root

# third way

# class Solution {
#     //int start = 0;
#     Map<Integer, Integer> map;
#     public TreeNode buildTree(int[] preorder, int[] inorder) {
#         //preorder root left right
#         //inorder left root right
#         if(preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0) return null;
#         map = new HashMap<>();
#         for(int i = 0; i < inorder.length; i ++){
#             map.put(inorder[i],i);
#         }
#         return helper(preorder,0, preorder.length - 1, inorder, 0, inorder.length - 1);
#     }
#
#     public TreeNode helper(int[]preorder,int startPre, int endPre, int[] inorder, int startIn, int endIn){
#         if(startIn > endIn || startPre > endPre){
#             return null;
#         }
#         int value = preorder[startPre];
#         TreeNode root = new TreeNode(value);
#         int index = map.get(value);
#         // for(int i = startIn; i <= endIn; i ++){
#         //     if(inorder[i] == value){
#         //         index = i;
#         //         break;
#         //     }
#         // }
#         int leftCount = index - startIn;
#         root.left = helper(preorder, startPre + 1,             startPre + leftCount, inorder, startIn,   index - 1);
#         root.right =helper(preorder, startPre + leftCount + 1, endPre,               inorder, index + 1, endIn);
#         return root;
#     }

# python solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# second way
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         idx = {inorder[i]: i for i in range(len(inorder))}
#
#         root_val = preorder[0]
#         root = TreeNode(root_val)
#         inorder_root_index = idx[root_val]
#
#         root.left = self.buildTree(preorder[1:inorder_root_index + 1], inorder[0: inorder_root_index])
#         root.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])
#
#         return root

# Third way
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        map = {inorder[i]: i for i in range(len(inorder))}

        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, map)

    def helper(self, preorder, p1, p2, inorder, i1, i2, map):
        if i1 > i2 or p1 > p2:
            return None

        root = TreeNode(preorder[p1])
        index = map[root.val]
        leftCount = index - i1
        # p1+1 to exclude the root at p1, compare with post order, uses p2 - 1, to exclude the root at p2
        root.left =  self.helper(preorder, p1 + 1,             p1 + leftCount,    inorder, i1,        index - 1, map)
        root.right = self.helper(preorder, p1 + leftCount + 1, p2,                inorder, index + 1, i2,        map)

        return root