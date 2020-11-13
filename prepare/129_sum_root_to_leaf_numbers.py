# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # put all root to leaf numbers in array
        if root == None:
            return 0

        self.result = []
        self.path = []
        self.dfs(root)

        totalSum = 0
        for items in self.result:
            sums = 0
            for item in items:
                sums = sums * 10 + item

            totalSum += sums

        return totalSum

    def dfs(self, root):

        if root.left == None and root.right == None: # leaf node
            self.path.append(root.val)
            self.result.append(self.path[:])
            self.path.pop()  # leaf
            return

        self.path.append(root.val)

        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

        self.path.pop()  # root