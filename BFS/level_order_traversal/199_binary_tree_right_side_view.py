# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# 199. Binary Tree Right Side View
# public class Q_0199_Binary_Tree_Right_Side_View {
#
#
#    public static void main(String[] args) {
#        Q_0199_Binary_Tree_Right_Side_View solution = new Q_0199_Binary_Tree_Right_Side_View();
#        TreeNode root = Util.buildTree("1,2,3,#,5,#,4,#,#,#,#");
#        System.out.println(solution.rightSideView(root));
#    }
#
#
#    public List<Integer> rightSideView(TreeNode root) {
#        List<Integer> res = new ArrayList<>();
#        if (root == null) {
#            return res;
#        }
#        Queue<TreeNode> q = new LinkedList<>();
#        q.offer(root);
#        while (!q.isEmpty()) {
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                TreeNode curr = q.poll();
#                if (i == 0) {
#                    res.add(curr.val);
#                }
#                if (curr.right != null) {
#                    q.offer(curr.right);
#                }
#                if (curr.left != null) {
#                    q.offer(curr.left);
#                }
#            }
#        }
#        return res;
#    }
# }
