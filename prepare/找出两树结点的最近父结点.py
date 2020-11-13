# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = None

        def dfs(root, p, q):
            cp, cq = False, False

            if not root:
                return False, False

            if root.val == p.val:
                cp = True
            if root.val == q.val:
                cq = True

            lcp, lcq = dfs(root.left, p, q)
            rcp, rcq = dfs(root.right, p, q)

            cp = (cp or lcp or rcp)
            cq = (cq or lcq or rcq)

            if not self.result and (cp and cq):
                self.result = root

            return cp, cq

        dfs(root, p, q)

        return self.result


root = list_to_root([3,5,1,6,2,0,8,null,null,7,4])
p = 6
q = 5