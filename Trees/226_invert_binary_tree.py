# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left)
        print(current.val)
        self.inorder(current.right)




nodeList = [4,2,7,1,3,6,9]
count = 1
# while root:
#     root.left = TreeNode(nodeList[count])
#     root.right = TreeNode(count+1)
#     root =


#first case
n1 = TreeNode(6)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(1)
n5 = TreeNode(5)
n6 = TreeNode(7)
n7 = TreeNode(10)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
root = n1
# second case
# root = TreeNode(1)
# root.left = TreeNode(2)

s = Solution()

new_root = s.invertTree(root)
print("root")
s.inorder(root)
print("new root")
s.inorder(new_root)