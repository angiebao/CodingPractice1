

#given a binary tree, return the inorder trversal of its nodes' value
#input [1, null,2,3]
#output [1,3,2]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, result):
        current = root
        if current:
            self.inorder(current.left, result)
            result.append(current.val)
            self.inorder(current.right, result)

    def inorderTraversal_recur(self, root): # time O(n), because T(n) = 2*T(n/2)+1, space , worst O(n), average O(log(n))
        result = []
        self.inorder(root, result)
        return result
        
    # iteratively solve
    #def inorderTraversal(self, root: TreeNode):

# iterative solution -------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        cur = root
        # 从root出发一路向左， 找第一个node
        while cur:
            stack.append(cur)
            cur = cur.left

        while stack:
            # O（h）
            cur = stack.pop()
            res.append(cur.val)
            # 往右一步 再一路向左， 找下一个node
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left

        return res



