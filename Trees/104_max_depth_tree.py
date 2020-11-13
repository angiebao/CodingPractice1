# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recusively
    def maxDepth(self, root: TreeNode) -> int: # time O(n), space O(n)
        if root==None:
            return 0

        if root:
            depth = max(self.maxDepth(root.left), self.maxDepth(root.right))+1
            return depth




root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(3)

s= Solution()
print(s.maxDepth(root1))