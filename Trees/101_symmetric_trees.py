#given a bonary tree check whether it is a mirrow of itself(symmetric arround its center)
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # time complexity O(n),  space complexity O(n) ?
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return False

        currentp = root.left
        currentq = root.right


        result = self.Symetric(currentp, currentq)
        return result

    def Symetric(self, p: TreeNode, q:TreeNode):

        if p and q:
            sym = self.Symetric(p.left, q.right)
            if not sym:
                return False
            if p.val != q.val:
                return False
            sym = self.Symetric(p.right, q.left)
            if not sym:
                return False
            else:
                return True
        elif p==None and q==None:
            return True
        else:
            return False



#breadth first
    def isSymmetric_iter(self, root: TreeNode) -> bool:
        if root == None:
            return True

        rootleft = root.left
        rootright = root.right

        if rootleft==None or rootright ==None:
            if rootleft==rootright:
                return True
            else:
                return False

        traversal_queue = deque([rootleft])
        traversal_queueR= deque([rootright])


        while len(traversal_queue) > 0 and len(traversal_queueR)>0:

            node = traversal_queue.popleft()
            nodeR = traversal_queueR.popleft()

            if nodeR==None or node ==None:
                if nodeR != node:
                    return False
                if nodeR == node:
                    continue
            else:
                if node.val != nodeR.val:
                    return False

                traversal_queue.append(node.left)

                traversal_queue.append(node.right)

                traversal_queueR.append(nodeR.right)

                traversal_queueR.append(nodeR.left)

        if len(traversal_queue) != len(traversal_queueR):
            return False

        return True



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right= TreeNode(3)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(3)

s= Solution()
print(s.isSymmetric(root1))
