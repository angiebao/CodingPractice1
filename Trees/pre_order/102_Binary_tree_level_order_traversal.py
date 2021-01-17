# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.dfs(root, 0, ans)

        return ans

    def dfs(self, node, level, ans):
        if not node:
            return
        if len(ans) <= level:
            ans.append([])

        ans[level].append(node.val)
        self.dfs(node.left, level + 1, ans)
        self.dfs(node.right, level + 1, ans)