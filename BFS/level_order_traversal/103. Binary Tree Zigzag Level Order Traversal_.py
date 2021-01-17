# public class Q_0103_Binary_Tree_Zigzag_Level_Order_Traversal {
#
#
#    public static void main(String[] args) {
#        Q_0103_Binary_Tree_Zigzag_Level_Order_Traversal solution = new Q_0103_Binary_Tree_Zigzag_Level_Order_Traversal();
#        TreeNode root = Util.buildTree("3,9,20,#,#,15,7,#,#,#,#");
#        System.out.println(solution.zigzagLevelOrder(root));
#    }
#
#
#    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
#        List<List<Integer>> res = new ArrayList<>();
#        if (root == null) {
#            return res;
#        }
#        boolean reverse = false;
#        Queue<TreeNode> q = new LinkedList<>();
#        q.offer(root);
#        while (!q.isEmpty()) {
#            LinkedList<Integer> list = new LinkedList<>();
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                TreeNode curr = q.poll();
#                if (!reverse) {
#                    list.addLast(curr.val);
#                } else {
#                    list.addFirst(curr.val);
#                }
#
#
#                if (curr.left != null) {
#                    q.offer(curr.left);
#                }
#                if (curr.right != null) {
#                    q.offer(curr.right);
#                }
#            }
#            res.add(list);
#            reverse = !reverse;
#        }
#        return res;
#    }
# }


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        reverse = False

        q = collections.deque()

        q.append(root)
        reverse = False
        while q:
            temp = collections.deque()
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if reverse:
                    temp.appendleft(curr.val)
                else:
                    temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            res.append(temp)
            reverse = not reverse
        return res
