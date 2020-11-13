# # 112. Path Sum
# # Easy
# #
# # 1644
# #
# # 463
# #
# # Add to List
# #
# # Share
# # Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# #
# # Note: A leaf is a node with no children.
# #
# # Example:
# #
# # Given the below binary tree and sum = 22,
# #
# #       5
# #      / \
# #     4   8
# #    /   / \
# #   11  13  4
# #  /  \      \
# # 7    2      1

# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int):
        self.res = False

        self.calcSum(root, sum, 0)
        return self.res

    def calcSum(self, root, target, sums):
        if not root or self.res:
            return

        sums += root.val
        if root.left is None and root.right is None and sums == target:
            self.res = True
            return
        self.calcSum(root.left, target, sums)
        self.calcSum(root.right, target, sums)


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

nodeList = [5,4,8,11,None,13,4,7,2,None,None,None,1]

root = list2tree(nodeList)
sums = 22
s= Solution()
print(s.hasPathSum(root,22))
