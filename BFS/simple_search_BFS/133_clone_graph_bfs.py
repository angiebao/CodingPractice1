# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
#
# Test case format:
#
# For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
#
# Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
#
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


# public class Q0133_Clone_Graph {
#
#
#    public Node cloneGraph(Node node) {
#        if (node == null) {
#            return null;
#        }
#
#
#        // find all nodes
#        Queue<Node> q = new LinkedList<>();
#        Set<Node> set = new HashSet<>();
#        q.offer(node);
#        set.add(node);
#        while (!q.isEmpty()) {
#            Node curr = q.poll();
#            for (Node next : curr.neighbors) {
#                if (set.add(next)) {
#                    q.offer(next);
#                }
#            }
#        }
#
#
#        // have all nodes in set and build mapping
#        Map<Node, Node> map = new HashMap<>();
#        for (Node curr : set) {
#            map.put(curr, new Node(curr.val));
#        }
#
#
#        for (Node n : set) {
#            Node newNode = map.get(n);
#            for (Node next : n.neighbors) {
#                newNode.neighbors.add(map.get(next));
#            }
#        }
#
#
#        return map.get(node);
#    }
#
#
#    private static class Node {
#        public int val;
#        public List<Node> neighbors;
#
#
#        public Node() {
#            val = 0;
#            neighbors = new ArrayList<Node>();
#        }
#
#
#        public Node(int _val) {
#            val = _val;
#            neighbors = new ArrayList<Node>();
#        }
#
#
#        public Node(int _val, ArrayList<Node> _neighbors) {
#            val = _val;
#            neighbors = _neighbors;
#        }
#    }
#
#
# }


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
        for neighbor in node.neighbors:
            if neighbor.val not in self.visited:
                new_node = Node(neighbor.val)
                self.visited[neighbor.val] = new_node
                clone.neighbors.append(new_node)
                self.dfs(neighbor, new_node)
            else:
                clone.neighbors.append(self.visited[neighbor.val])

# bfs
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        visited = dict()
        visited[node] = Node(node.val)

        queue = collections.deque([node])
        while queue:

            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # connect the node to its neighbors no matter the neighbor is visted or not
                visited[cur].neighbors.append(visited[neighbor])

        return visited[node]
