# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # method 1 check pre order and in order traversal, if both comparision passed, then these two tree are identical
    # method2 , check in order at the same time
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        currentp = p
        currentq = q

        if currentp and currentq:
            same = self.isSameTree(currentp.left, currentq.left)
            if not same:
                return False

            if currentp.val != currentq.val:
                return False

            same = self.isSameTree(currentp.right, currentq.right)
            if not same:
                return False
            else:
                return True
        elif (currentp == None)  and (currentq == None):
            return True
        else:
            return False
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

s = Solution()

print(s.isSameTree(root1, root2))