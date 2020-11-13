class TreeNode:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.value = x

def buildTree(i, nodeList):
    result = []
    for edge in edges:
        if edge[0] == nodeList[i].value:
            result.append(edge[1])

    if result:
        nodeList[i].left = nodeList[result[0]]
        nodeList[i].right = nodeList[result[1]]

        buildTree(nodeList[i].left.value,nodeList)
        buildTree(nodeList[i].right.value,nodeList)



edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
n = len(hasApple)
nodeList = []
nodeList = []
for i in range(n):
    nodeList.append(TreeNode(i))

buildTree(0, nodeList)

print(nodeList[0].value)


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x


# class Solution:
#
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         self.hasApple = hasApple
#         self.edges = edges
#         n = len(hasApple)
#         nodeList = []
#         for i in range(n):
#             nodeList.append(TreeNode(i))
#
#         root = buildTree(nodeList[0], nodeList)
#         dfs()
#
#     def buildTree(self, root, nodeList, edges):
#
#         for edge in edges:
#             if edge[0] == root.value:
#                 result.append(edge[1])
#
#         if res not empty:
#             root.left = nodeList[result[0]]
#             root.right = nodeList[result[1]]
#
#             buildTree(root.left)
#             buildTree(root.right)
#
#         for i in range(len(self.edges)):
#             root = TreeNode(edges[i][0])
#             root.left = edges[i][1]
#             for
#                 root.right = edges[i + 1][1]
#
#     def dfs(self, )