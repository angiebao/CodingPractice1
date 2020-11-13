# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        #         def helper(in_left = 0, in_right = len(preorder)):
        #             nonlocal pre_idx
        #             # if there is no elements to construct subtrees
        #             if in_left == in_right:
        #                 return None

        #             # pick up pre_idx element as a root
        #             root_val = preorder[pre_idx]
        #             root = TreeNode(root_val)

        #             # root splits inorder list
        #             # into left and right subtrees
        #             index = idx_map[root_val]

        #             # recursion
        #             pre_idx += 1
        #             # build left subtree
        #             root.left = helper(in_left, index)
        #             # build right subtree
        #             root.right = helper(index + 1, in_right)
        #             return root

        #         inorder = sorted(preorder)
        #         # start from first preorder element
        #         pre_idx = 0
        #         # build a hashmap value -> its index
        #         idx_map = {val:idx for idx, val in enumerate(inorder)}
        #         return helper()
        n = len(preorder)
        self.preorder = preorder
        self.inorder = sorted(preorder)  # O(NlogN)
        self.inorder_map = {val: idx for idx, val in enumerate(self.inorder)}

        return self.buildTree(0, n, 0, n)

    def buildTree(self, pre_start, pre_end, in_start, in_end):
        # set the termiantion condition
        if pre_start + 1 == pre_end:
            return None
        # find the index for the root node in inorder

        in_idx = self.inorder_map[self.preorder[pre_start]]
        root_val = self.preorder[pre_start]
        root = TreeNode(root_val)
        # next element in preorder


        root.left = self.buildTree(pre_start + 1,                      pre_start + 1 + in_idx - in_start,   in_start,     in_idx)
        root.right = self.buildTree(pre_start + in_idx - in_start + 1,  pre_end,                             in_idx + 1,   in_end)

        return root
preOrder = [8,5,1,7,10,12]
s = Solution()
s.bstFromPreorder(preOrder)