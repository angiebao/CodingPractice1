# null tree
# parent node?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        res = self.helper(root)
        return res[1]

    def helper(self, root):
        if not root:
            return (0, True)

        left = self.helper(root.left)
        right = self.helper(root.right)
        if (not left[1]) or (not right[1]) or abs(left[0] - right[0]) > 1:
            return (0, False)
        return (max(left[0], right[0]) + 1, True)

