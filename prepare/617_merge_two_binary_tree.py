# 617. Merge Two Binary Trees
# Easy
#
# 2726
#
# 162
#
# Add to List
#
# Share
# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # the hardest part is if there is a node is null, but other is not, how to combine them? add a parent variable or ?
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def helper(root1, root2):

            if root1 is None and root2 is None:
                return
            elif root1 is None and root2 is not None:
                iterRoot = TreeNode(root2.val)

                iterRoot.left = helper(None,
                                       root2.left)  # sub problem is left node point to the root of the left sub tree

                iterRoot.right = helper(None,
                                        root2.right)  # sub problem is right node point to the root of the right sub tree

            elif root1 is not None and root2 is None:
                iterRoot = TreeNode(root1.val)

                iterRoot.left = helper(root1.left, None)

                iterRoot.right = helper(root1.right, None)

            else:
                iterRoot = TreeNode(root1.val + root2.val)

                iterRoot.left = helper(root1.left, root2.left)

                iterRoot.right = helper(root1.right, root2.right)

            return iterRoot  # return to iterRoot.left or iterRoot.right

        return helper(t1, t2)


