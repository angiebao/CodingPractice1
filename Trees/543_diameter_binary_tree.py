# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if root == None:
            return 0
        h1 = self.diameterHelper(root)

        return self.diameter

    def diameterHelper(self, root: TreeNode):
        if root:
            h1 = self.diameterHelper(root.left)
            h2 = self.diameterHelper(root.right)
            h = h1 + h2
            if h >= self.diameter:
                self.diameter = h
            return max(h1, h2)+1

        else:
            return 0


#first case
n1 = TreeNode(6)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(1)
n5 = TreeNode(5)
n6 = TreeNode(7)
n7 = TreeNode(10)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

#second case
nodeList = [ 3, 1, None, None, 2]
def list2tree(l):
    if not l:
        return None
    root = TreeNode(l[0])
    q = collections.deque([(root, 'left'), (root, 'right')])
    i = 1
    while i < len(l):
        cur = q.popleft()
        value = l[i]
        if value is not None:
            if cur[1] == 'left':
                cur[0].left = TreeNode(value)
                q.append((cur[0].left, 'left'))
                q.append((cur[0].left, 'right'))
            else:
                cur[0].right = TreeNode(value)
                q.append((cur[0].right, 'left'))
                q.append((cur[0].right, 'right'))
        i += 1

    return root


root = list2tree(nodeList)


s = Solution()
print(s.diameterOfBinaryTree(root))


