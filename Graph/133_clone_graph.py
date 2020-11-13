
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    # dfs
    def cloneGraph(self, node):
        clone = None
        if node:
            clone = Node(node.val)
            self.visited = {node.val: clone}
            self.dfs(node, clone)

        return clone

    def dfs(self, node, clone):
        for n in node.neighbors:
            if n.val not in self.visited:
                new_node = Node(n.val)
                self.visited[n.val] = new_node
                clone.neighbors.append(new_node)
                self.dfs(n, new_node)
            else:
                clone.neighbors.append(self.visited[n.val])