

# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) :
        self.flag = False
        self.result = []
        self.calcSum(root, sum, 0, [])
        return self.result

    def calcSum(self, root, target, sums, res):
        if not root:
            return
        sums += root.val
        res.append(root.val)

        if root.left is None and root.right is None and sums == target:
            self.flag = True
            self.result.append(res.copy())
            #return # this cannot be returned directory, otherwise, the leaf "2" cannot be removed at this layer

        self.calcSum(root.left, target, sums, res)
        self.calcSum(root.right, target, sums, res)
        res.pop()



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

nodeList = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = list2tree(nodeList)
sums = 22
s= Solution()
results =s.pathSum(root,22)
print(results)
