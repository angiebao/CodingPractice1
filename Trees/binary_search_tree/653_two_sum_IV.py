# public class Q_0653_Two_Sum_IV_Input_is_a_BST {
#
#    public static void main(String[] args) {
#        Q_0653_Two_Sum_IV_Input_is_a_BST solution = new Q_0653_Two_Sum_IV_Input_is_a_BST();
#        TreeNode root = Util.buildTree("5,3,6,1,4,#,7,#,#,#,#,#,#");
#        int k1 = 9;
#        int k2 = 28;
#        System.out.println(solution.findTarget1(root, k1));
#        System.out.println(solution.findTarget1(root, k2));
#        Util.printSeparator();
#        System.out.println(solution.findTarget2(root, k1));
#        System.out.println(solution.findTarget2(root, k2));
#        Util.printSeparator();
#        System.out.println(solution.findTarget3(root, k1));
#        System.out.println(solution.findTarget3(root, k2));
#    }
#
#    // Solution 1:
#    // Using HashSet and pre-order traversal, no BST property utilized
#    public boolean findTarget1(TreeNode root, int k) {
#        Set<Integer> set = new HashSet<>();
#        return dfs1(root, set, k);
#    }
#
#    private boolean dfs1(TreeNode root, Set<Integer> set, int k) {
#        if (root == null) {
#            return false;
#        }
#        if (set.contains(k - root.val)) {
#            return true;
#        }
#        set.add(root.val);
#        return dfs1(root.left, set, k) || dfs1(root.right, set, k);
#    }
#
#    // Solution 2:
#    // Utilizing BST property and in-order traversal
#    public boolean findTarget2(TreeNode root, int k) {
#        List<Integer> list = new ArrayList<>();
#        inorder(root, list);
#        int i = 0;
#        int j = list.size()-1;
#        while (i < j) {
#            int sum = list.get(i) + list.get(j);
#            if (sum < k) {
#                i++;
#            } else if (sum > k) {
#                j--;
#            } else {
#                return true;
#            }
#        }
#        return false;
#    }
#    private void inorder(TreeNode root, List<Integer> list) {
#        if (root == null) {
#            return;
#        }
#        inorder(root.left, list);
#        list.add(root.val);
#        inorder(root.right, list);
#    }

#    // Solution 3:
#    // Utilizing BST property and recursive call

#
#    public boolean findTarget3(TreeNode root, int k) {
#        return dfs3(root, root, k);
#    }
#
#    private boolean dfs3(TreeNode root, TreeNode curr, int k) {
#        if (curr == null) {
#            return false;
#        }
#        if (search(root, curr, k-curr.val)) {
#            return true;
#        }
#        return dfs3(root, curr.left, k) || dfs3(root, curr.right, k);
#    }
#
#    private boolean search(TreeNode root, TreeNode curr, int val) {
#        if (root == null) {
#            return false;
#        }
#        if (val < root.val) {
#            return search(root.left, curr, val);
#        } else if (val > root.val) {
#            return search(root.right, curr, val);
#        } else {
#            return root != curr; // notice the same element should not be used twice
#        }
#    }
# }

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:135
    def findTarget(self, root: TreeNode, k: int) -> bool:
       # using BST property and in order traversal
        array = []
        self.inorder(root, array)
        i = 0
        j = len(array) - 1
        while i< j:
            sum = array[i] + array[j]
            if sum < k:
                i+=1
            elif sum > k:
                j-=1
            else:
                return True
        return False
    def inorder(self, root, array):
        if root is None:
            return
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)