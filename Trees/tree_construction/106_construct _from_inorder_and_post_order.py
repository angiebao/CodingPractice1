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

