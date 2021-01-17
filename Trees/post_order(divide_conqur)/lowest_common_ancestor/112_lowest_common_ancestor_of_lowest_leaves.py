# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
#
# Recall that:
#
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
# Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
#
#
#
# Example 1:
#

  #     3
  #     /\
  #   5   1
  # /\    /\
  # 6 2   0 8
  #   /\
  #   7 4
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
# Example 2:
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree, and it's the lca of itself.
# Example 3:
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# method 1
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.levels = []
        self.level_order(root, 0)
        print(self.levels[-1])
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return None, 0

        left_ans, left_h = self.helper(root.left)
        right_ans, right_h = self.helper(root.right)

        # conquer
        # left_h ==right_h ans = root
        # left_h > right_h ans = left_ans
        # lefth >  right_h  ans = right_ans

        if left_h == right_h:
            return root, left_h + 1

        if left_h < right_h:
            return right_ans, right_h + 1

        return left_ans, left_h + 1

    def level_order(self, root, depth):
        if not root:
            return
        if depth == len(self.levels):
            self.levels.append([])
        self.levels[depth].append(root)
        self.level_order(root.left, depth + 1)
        self.level_order(root.right, depth + 1)

# method 2:
# find the lowest leaves and the find their ancestor



