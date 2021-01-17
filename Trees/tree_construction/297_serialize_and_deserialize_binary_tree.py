# serialization: 1. store:  convert the object to string, store the value in a format suitable for hardware store,
#                2. transmission, for example to transform data to google cloud.

# deserialize : 1. convert string to object to store in memory
#               2.
# public class Q_0297_Serialize_and_Deserialize_Binary_Tree {
#
#
#    public static void main(String[] args) {
#
#
#        TreeNode root = new TreeNode(1);
#        root.left = new TreeNode(2);
#        root.right = new TreeNode(3);
#        root.right.left = new TreeNode(4);
#        root.right.right = new TreeNode(5);
#
#
#        String serialized1 = serialize1(root);
#        System.out.println(serialized1);
#        TreeNode deserialized1 = deserialize1(serialized1);
#        System.out.println(deserialized1);
#
#
#        String serialized2 = serialize2(root);
#        System.out.println(serialized2);
#        TreeNode deserialized2 = deserialize2(serialized2);
#        System.out.println(deserialized2);
#
#
#        TreeNode root1 = new TreeNode(3);
#        root1.left = new TreeNode(5);
#        root1.right = new TreeNode(1);
#        root1.left.left = new TreeNode(6);
#        root1.left.right = new TreeNode(2);
#        root1.right.left = new TreeNode(0);
#        root1.right.right = new TreeNode(8);
#        root1.left.right.left = new TreeNode(7);
#        root1.left.right.right = new TreeNode(4);
#
#
#        String serialized3 = serialize1(root1);
#        System.out.println(serialized3);
#
#
#        List<Integer> serialized4 = serialize3(root);
#        System.out.println(serialized4);
#        Util.printTree(deserialize3(serialized4));
#
#
#        List<Integer> serialized5 = serialize3(root1);
#        System.out.println(serialized5);
#        Util.printTree(deserialize3(serialized5));
#    }
#
#
#    /**********************************************************************
#                        BFS  - non-recursive approach
#     **********************************************************************/
#
#
#    // Encodes a tree to a single string.
#    public static String serialize1(TreeNode root) {
#        if (root == null) {
#            return "";
#        }
#        List<String> list = new ArrayList<>();
#        Queue<TreeNode> q = new LinkedList<>();
#        q.offer(root);
#        while (!q.isEmpty()) {
#            TreeNode curr = q.poll();
#            if (curr != null) {
#                q.offer(curr.left); // 有可能把空节点放到q中
#                q.offer(curr.right);
#                list.add(curr.val + "");
#            } else {
#                list.add("#");
#            }
#        }
#        return Joiner.on(",").join(list);
#    }
#
#
#    // Decodes your encoded data to tree.
#    public static TreeNode deserialize1(String data) {
#        if (data.isEmpty()) return null;
#
#
#        String[] nodes = data.split(",");
#        Queue<TreeNode> q = new LinkedList<>();
#        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
#        q.offer(root);
#        int index = 1;
#        while (!q.isEmpty()) {
#            TreeNode curr = q.poll();
#            if (!nodes[index].equals("#")) {
#                curr.left = new TreeNode(Integer.parseInt(nodes[index]));
#                q.offer(curr.left);
#            }
#            index++;
#            if (!nodes[index].equals("#")) {
#                curr.right = new TreeNode(Integer.parseInt(nodes[index]));
#                q.offer(curr.right);
#            }
#            index++;
#        }
#        return root;
#    }
#
#
#    /**********************************************************************
#                        DFS  - recursive approach
#     **********************************************************************/
#    public static String serialize2(TreeNode root) {
#        StringBuilder sb = new StringBuilder();
#        ser_helper(root, sb);
#        return sb.toString();
#    }
#
#
#    private static void ser_helper(TreeNode root, StringBuilder sb) {
#        if (root == null) {
#            if (sb.length() > 0) {
#                sb.append(",");
#            }
#            sb.append("#");
#            return;
#        }
#        if (sb.length() > 0) {
#            sb.append(",");
#        }
#        sb.append(root.val);
#        ser_helper(root.left, sb);
#        ser_helper(root.right, sb);
#    }
#
#
#    // Decodes your encoded data to tree.
#    public static TreeNode deserialize2(String data) {
#        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(",")));
#        TreeNode node = deser_helper(q);
#        return node;
#    }
#
#
#    private static TreeNode deser_helper(Queue<String> q) {
#        String curr = q.poll();
#        if (curr.equals("#")) return null;
#        TreeNode root = new TreeNode(Integer.parseInt(curr));
#        root.left = deser_helper(q);
#        root.right = deser_helper(q);
#        return root;
#    }
#
#
#    /**********************************************************************
#                Use preorder and inorder to reconstruct tree
#     **********************************************************************/
#    public static List<Integer> serialize3(TreeNode root) {
#        List<Integer> res = new ArrayList<>();
#        List<Integer> preorder = preorder(root);
#        List<Integer> inorder = inorder(root);
#        res.addAll(preorder);
#        res.addAll(inorder);
#        return res;
#    }
#
#
#    public static TreeNode deserialize3(List<Integer> list) {
#        List<Integer> preorder = new ArrayList<>();
#        List<Integer> inorder = new ArrayList<>();
#        for (int i = 0; i < list.size(); i++) {
#            if (i < list.size() / 2) {
#                preorder.add(list.get(i));
#            } else {
#                inorder.add(list.get(i));
#            }
#        }
#        return constructTreeByPreorderAndInorder(preorder, inorder);
#    }
#
#
#    private static List<Integer> inorder(TreeNode root) {
#        List<Integer> res = new ArrayList<>();
#        inorderHelper(root, res);
#        return res;
#    }
#
#
#    private static void inorderHelper(TreeNode root, List<Integer> res) {
#        if (root == null) {
#            return;
#        }
#        inorderHelper(root.left, res);
#        res.add(root.val);
#        inorderHelper(root.right, res);
#    }
#
#
#    private static List<Integer> preorder(TreeNode root) {
#        List<Integer> res = new ArrayList<>();
#        preorderHelper(root, res);
#        return res;
#    }
#
#
#    private static void preorderHelper(TreeNode root, List<Integer> res) {
#        if (root == null) {
#            return;
#        }
#        res.add(root.val);
#        preorderHelper(root.left, res);
#        preorderHelper(root.right, res);
#    }
#
#
#    private static TreeNode constructTreeByPreorderAndInorder(List<Integer> preorder, List<Integer> inorder) {
#        Map<Integer, Integer> map = new HashMap<>();
#        for (int i = 0; i < inorder.size(); i++) {
#            map.put(inorder.get(i), i);
#        }
#        return helper(preorder, 0, 0, preorder.size()-1, map);
#    }
#
#
#    private static TreeNode helper(List<Integer> preorder, int index, int start, int end, Map<Integer, Integer> map) {
#        if (start > end) {
#            return null;
#        }
#        int rootIndex = map.get(preorder.get(index));
#        TreeNode root = new TreeNode(preorder.get(index));
#        root.left = helper(preorder, index+1, start, rootIndex-1, map);
#        root.right = helper(preorder, index+(rootIndex-start)+1, rootIndex+1, end, map);
#        return root;
#    }
# }

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
'''
   1
   2  3
      4 5
[1, 2,  # , #,  3, 4,#, #, 5, #, #]
 Tree node-> left, right, val

Q[  # ,#,4,5]
    Res

Root = TreeNode(1)
Res = [1]

Root = TreeNode(2)
Res = [1, 2]

Root = none
Res = [1, 2 ，  # ]

Root = none
Res = [1, 2,  # , #]

       Root = 3
Res = [1, 2,  # , #, 3]

       Root = 4
Res = [1, 2  # ， #, 4 ]
'''
def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        sb = []
        self.ser_helper(root, sb)
        return "".join(sb)

    def ser_helper(self, root, sb):
        if root is None:
            if len(sb) > 0:
                sb.append(",")
            # "#" is represented as a none node
            sb.append("#")
            return
        if len(sb) > 0:
            # "," is used to split the string later
            sb.append(",")

        sb.append(str(root.val))
        self.ser_helper(root.left, sb)
        self.ser_helper(root.right, sb)

'''
    Res = [1, 2,  # , #,  3, 4,#, #, 5, #, #]

           q = 1
    2  # #   3  4 # # 5  #  #
    cur = 1, q = 2  # # 3 4 # # 5 # #
    Root = treeNode(1)

    left
    cur = 2, q = 2  # # 3 4 # # 5 # #
    Root = treeNode(2)
    root.left = None(cur=  # )
                     root.right = None(cur=  # )
    return 2
    / \
            None
    None


right
Cur = 3, q = 4  # # 5 # #


'''

def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        q = collections.deque(data.split(","))
        node = self.deser_helper(q)
        return node

    def deser_helper(self, q):
        curr = q.popleft()
        if curr == "#":
            return None
        root = TreeNode(int(curr))
        root.left = self.deser_helper(q)
        root.right = self.deser_helper(q)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))