# public class Q_0323_Number_of_Connected_Components_in_an_Undirected_Graph {
#
#
#    public static void main(String[] args) {
#        Q_0323_Number_of_Connected_Components_in_an_Undirected_Graph solution = new Q_0323_Number_of_Connected_Components_in_an_Undirected_Graph();
#
#
#        int n1 = 5;
#        int[][] edges1 = {{0, 1}, {1, 2}, {3, 4}};
#        int n2 = 5;
#        int[][] edges2 = {{0, 1}, {1, 2}, {2, 3}, {3, 4}};
#
#
#        System.out.println(solution.countComponents1(n1, edges1));
#        System.out.println(solution.countComponents1(n2, edges2));
#        System.out.println(solution.countComponents2(n1, edges1));
#        System.out.println(solution.countComponents2(n2, edges2));
#    }
#
#
#    public int countComponents1(int n, int[][] edges) {
#        Map<Integer, Set<Integer>> map = new HashMap<>();
#        init(n, edges, map);
#
#
#        int cnt = 0;
#        boolean[] visited = new boolean[n];
#        for (int i = 0; i < n; i++) {
#            if (!visited[i]) {
#                cnt++;
#                bfs(i, map, visited);
#            }
#        }
#        return cnt;
#    }
#
#
#    public int countComponents2(int n, int[][] edges) {
#        Map<Integer, Set<Integer>> map = new HashMap<>();
#        init(n, edges, map);
#
#
#        int cnt = 0;
#        boolean[] visited = new boolean[n];
#        for (int i = 0; i < n; i++) {
#            if (!visited[i]) {
#                cnt++;
#                dfs(i, map, visited);
#            }
#        }
#        return cnt;
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
#
#    private void bfs(int i, Map<Integer, Set<Integer>> map, boolean[] visited) {
#        Queue<Integer> q = new LinkedList<>();
#        q.offer(i);
#        visited[i] = true;
#        while (!q.isEmpty()) {
#            int curr = q.poll();
#            for (int next : map.get(curr)) {
#                if (!visited[next]) {
#                    q.offer(next);
#                    visited[next] = true;
#                }
#            }
#        }
#    }
#
#
#    private void init(int n, int[][] edges, Map<Integer, Set<Integer>> map) {
#        for (int i = 0; i < n; i++) {
#            map.put(i, new HashSet<>());
#        }
#        for (int[] e : edges) {
#            map.get(e[0]).add(e[1]);
#            map.get(e[1]).add(e[0]);
#        }
#    }
# }


import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        maps = collections.defaultdict(set)
        self.init(n, edges, maps)

        cnt = 0
        visited = [False for i in range(n)]
        for i in range(n):
            if not visited[i]:
                cnt += 1
                self.dfs(i, maps, visited)

        return cnt

    def dfs(self, curr, maps, visited):
        visited[curr] = True
        for nxt in maps[curr]:
            if not visited[nxt]:
                self.dfs(nxt, maps, visited)

    def init(self, n, edges, maps):

        # for i in range(n):
        #     maps[i] = set()
        for e in edges:
            maps[e[0]].add(e[1])
            maps[e[1]].add(e[0])





# for 
