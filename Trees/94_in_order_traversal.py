#given a binary tree, return the inorder trversal of its nodes' value
#input [1, null,2,3]
#output [1,3,2]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class List:
    def __init__(self):
        self = []

class Solution:
    def inorder(self, root: TreeNode, result):
        current = root
        if current:
            self.inorder(current.left, result)
            result.append(current.val)
            self.inorder(current.right, result)

    def inorderTraversal_recur(self, root: TreeNode): # time O(n), because T(n) = 2*T(n/2)+1, space , worst O(n), average O(log(n))
        result = []
        self.inorder(root, result)
        return result
        
    # iteratively solve
    #def inorderTraversal(self, root: TreeNode):







root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


s = Solution()
listnodes = s.inorderTraversal(root)
for i in range(0, len(listnodes)):
    node = listnodes[i]
    print(node)
