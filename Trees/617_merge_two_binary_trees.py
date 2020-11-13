# Given two binary trees and imagine that when you put one of them to cover the other,
# some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if t1 or t2:
            if not t1:
                t1 = TreeNode(0)
            if not t2:
                t2 = TreeNode(0)
            t1.val = t1.val + t2.val

            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)

            return t1
        return None



#second case
import collections
nodeList1 = [1,3,2,5]
nodeList2= [2,1,3,None,4,None,7]
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

def breadth_first_traversal(root_node):
    list_of_nodes = []
    traversal_queue = collections.deque([root_node])

    while len(traversal_queue)>0:
        node = traversal_queue.popleft() # 双向队列, root_node
        list_of_nodes.append(node)
        if node == None:
            print("None")
        print(node.val)

        if node.left:
            traversal_queue.append(node.left)
            #print(node.left_child.data)

        if node.right:
            traversal_queue.append(node.right)
            #print(node.right_child.data)

    return list_of_nodes

root1 = list2tree(nodeList1)
root2 = list2tree(nodeList2)


s = Solution()
newRoot = s.mergeTrees(root1, root2)
breadth_first_traversal(newRoot)


