# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# public class Q_0102_Binary_Tree_Level_Order_Traversal {
#
#
#    public static void main(String[] args) {
#        Q_0102_Binary_Tree_Level_Order_Traversal solution = new Q_0102_Binary_Tree_Level_Order_Traversal();
#        TreeNode root = Util.buildTree("3,9,20,#,#,15,7,#,#,#,#");
#        System.out.println(solution.levelOrder(root));
#    }
#
#
#    public List<List<Integer>> levelOrder(TreeNode root) {
#        List<List<Integer>> res = new ArrayList<>();
#        if (root == null) {
#            return res;
#        }
#        Queue<TreeNode> q = new LinkedList<>();
#        q.offer(root);
#        while (!q.isEmpty()) {
#            List<Integer> list = new ArrayList<>();
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                TreeNode curr = q.poll();
#                list.add(curr.val);
#                if (curr.left != null) {
#                    q.offer(curr.left);
#                }
#                if (curr.right != null) {
#                    q.offer(curr.right);
#                }
#            }
#            res.add(list);
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            l = []
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                l.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(l)

        return res


# could use dfs aS well

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.dfs(root, 0, ans)

        return ans

    def dfs(self, node, level, ans):
        if not node:
            return
        if len(ans) - 1 < level:
            ans.append([])

        ans[level].append(node.val)
        self.dfs(node.left, level + 1, ans)
        self.dfs(node.right, level + 1, ans)