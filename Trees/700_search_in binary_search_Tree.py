# Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode: #time complexity, worst O(n), space O(1)
        current = root
        while True:
            if current is None:
                return None
            elif current.val == val:
                return current
            elif current.val > val:
                current = current.left
            elif current.val<val:
                current= current.right

