# 261. Graph Valid Tree
# public class Q_0261_Graph_Valid_Tree {
#
#
#    public boolean validTree(int n, int[][] edges) {
#        // two conditions need to be satisfied with for a valid tree
#        // 1. number of nodes == number of edges + 1;
#        // 2. only on connected component
#
#
#        if (edges.length + 1 != n) {
#            return false;
#        }
#
#
#        Map<Integer, Set<Integer>> map = new HashMap<>();
#        init(n, edges, map);
#
#
#        int cnt = 0;
#        boolean[] visited = new boolean[n];
#        for (int i = 0; i < n; i++) {
#            if (!visited[i]) {
#                dfs(i, map, visited);
#                cnt++;
#            }
#        }
#        return cnt == 1;
#    }
#
#
#    private void dfs(int curr, Map<Integer, Set<Integer>> map, boolean[] visited) {
#        visited[curr] = true;
#        for (int next : map.get(curr)) {
#            if (!visited[next]) {
#                dfs(next, map, visited);
#            }
#        }
#    }
#
import collections
def validTree(n, edges):
    if len(edges) +1 != n:
        return False

    map = collections.defaultdict(set)
    self.init(n, edges, map)
    cnt = 0
    visited = [false for i in range(n)]
    for i in range(len(n):
        if not visited[i]:
            dfs(i, map, visited))
            cnt += 1
    return cnt == 1 # means all connected

    self.dfs(cur, map, visited):
    visited[curr] = true
    for nxt in map[curr]:
        if not visted[nxt]:
            dfs(nxt, map, visited)


def init(self, edges, map):
    for e in edges:
        map[e[0]].add(e[1])
        map[e[1]].add(e[0])
#
#    private void init(int n, int[][] edges, Map<Integer, Set<Integer>> map) {
#        // since some nodes might not appear in the edges so it must be initialized first
#        // like course schedule problem
#        for (int i = 0; i < n; i++) {
#            map.put(i, new HashSet<>());
#        }
#        for (int[] e : edges) {
#            map.get(e[0]).add(e[1]);
#            map.get(e[1]).add(e[0]);
#        }
#    }
# }



# graph to be valid tree->
# all nodes connected :  one component(number of connected component)
# no circle:               number of nodes =  edges + 1








