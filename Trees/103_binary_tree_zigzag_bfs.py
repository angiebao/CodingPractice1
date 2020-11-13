# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        level = 0
        q.append((root, level))
        list_of_node = collections.defaultdict(list)

        while q:
            node, level = q.popleft()
            list_of_node[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        result = []
        i = 0
        for key, value in list_of_node.items():
            if i % 2 == 0:
                result.append(value)
            else:
                result.append(value[::-1])
            i += 1
        return result
