# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4

 # method 1 iteration

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        res = root.val
        while root:
            if not root:
                return 0
            if abs(root.val - target) < abs(res - target):
                res = root.val

            if root.val < target:
                root = root.right

            elif root.val > target:
                root = root.left
            else:
                return root.val

        return res

# method 2 : dfs


