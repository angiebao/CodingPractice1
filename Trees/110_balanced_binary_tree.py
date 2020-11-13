# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #bottom up recursion time complexity O(n)? space O(n)
    def isBalanced_bottomup(self, root: TreeNode) -> bool:
        if root == None:
            return True
        result, h = self.checkBalance(root)
        return result

    def checkBalance (self, root: TreeNode):
        if root:
            result1, h1= self.checkBalance(root.left)
            result2, h2 = self.checkBalance(root.right)
            if result1 and result2:
                diff = max(h1,h2) - min(h1, h2)
                if diff <=1:
                    return True, max(h1, h2)+1
                else:
                    return False, max(h1, h2)+1
            else:
                return False, max(h1, h2)+1
        else:
            return True, 0


    #top down method, time complexity is O(n log n), space complexity is O（n）
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(3)

s= Solution()
print(s.isBalanced(root1))