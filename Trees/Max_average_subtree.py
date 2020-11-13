class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAverage(self, root: TreeNode) -> TreeNode:
        self.maxAvg = float('-inf')
        if root == None:
            return 0
        self.helper(root)

        return self.maxAvg
    def helper(self, root):

        if root.left ==None and root.right ==None:
            return 1, root.val


        if root.left:
            leftcount, leftSum = self.helper(root.left)

        if root.right:
            rightcount, rightSum = self.helper(root.right)

        curSum = leftSum + rightSum + root.val
        count = (leftcount + rightcount + 1)

        curAvg = curSum/count
        if curAvg > self.maxAvg:
            self.maxAvg = curAvg

        return count , curSum


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
root = n1

s= Solution()
print(s.maxAverage(root))
