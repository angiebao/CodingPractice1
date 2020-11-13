# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        idx = {inorder[i]: i for i in range(len(inorder))}

        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_root_index = idx[root_val]

        root.left = self.buildTree(preorder[1:inorder_root_index + 1], inorder[0: inorder_root_index])
        root.right = self.buildTree(preorder[inorder_root_index + 1:], inorder[inorder_root_index + 1:])

        return root

#         self.preorder = preorder
#         self.inorder = inorder
#         self.idx = {inorder[i]:i for i in range(len(inorder))}

#         inorder_left = 0
#         inorder_right = len(inorder)

#         self.pre_order_root_index = 0

#         return  self.helper(inorder_left, inorder_right)

#     def helper(self, inorder_left, inorder_right):
#         if inorder_left == inorder_right:
#             return None

#         root_value = self.preorder[self.pre_order_root_index]

#         root = TreeNode(root_value)
#         inorder_root_index  = self.idx[root_value]

#         self.pre_order_root_index += 1

#         # build right tree
#         root.left = self.helper(inorder_left, inorder_root_index)

#         # build left tree
#         root.right = self.helper(inorder_root_index+1 , inorder_right)

#         return root