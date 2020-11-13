# There are N cities numbered from 1 to N.
#
# You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
#
# Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.
#
#
#
# Example 1:
#
#
#[point a, point b, weight]
# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation:
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
# Example 2:
#
#
#
# Input: N = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation:
# There is no way to connect all cities even if all edges are used.
#
#
# Note:
#
# 1 <= N <= 10000
# 1 <= connections.length <= 10000
# 1 <= connections[i][0], connections[i][1] <= N
# 0 <= connections[i][2] <= 10^5
# connections[i][0] != connections[i][1]

import collections
# connections = [[1,2,5],[1,3,6],[2,3,1]]
# graph = collections.defaultdict(list)
# for item in connections:
#     graph[item[0]].append((item[1],item[2]))
#     graph[item[1]].append((item[0], item[2]))
#
# print(item[0])
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # prime's algorithm,use dictionary for graph and use heapImpl to store the weight related tuple (w, n)
        # TIME O((V+E)logV)
        #         if len(connections) == 0:
        #             return 0

        #         pq = []
        #         visited = set()
        #         visited.add(1)
        #         res = 0

        #         graph = collections.defaultdict(list)
        #         for (u, v, w) in connections:
        #             graph[u].append((v,w))
        #             graph[v].append((u, w))

        #         for (n, w) in graph[1]:
        #             heapq.heappush(pq, (w,n)) # possible to change to [w, n] ? yes

        #         while len(pq) > 0:
        #             cur = heapq.heappop(pq) # pop from head, head is the smallest one
        #             if cur[1] not in visited:
        #                 visited.add(cur[1])
        #                 res += cur[0]
        #                 for (n,w) in graph[cur[1]]: # O((V+E)logV)
        #                     if n not in visited:
        #                         heapq.heappush(pq,(w, n))  #O(logV)

        #         if len(visited) == N:
        #             return res
        #         else:
        #             return -1

        # Kruskal's algorithm,disjoint set to solve the union find problem, this is a union find problem because, if a node exist in the union, we will not chose it, so that we avoid making loops
        # Time O(Elog(E)+E), space( O(V))  from parent array
        if len(connections) == 0:
            return 0
        res = 0
        self.parents = [i for i in range(N)]

        connections.sort(key=lambda x: x[2])  # O(NlogN)

        for (u, v, w) in connections:  # O(N)
            if not self.is_connected(u - 1, v - 1):
                self.merge(u - 1, v - 1)
                res += w

        groups = {self.findParent(x) for x in self.parents}
        return res if len(groups) == 1 else -1

    def is_connected(self, u, v):
        return self.findParent(u) == self.findParent(v)

    def findParent(self, a):  # O(1)->O(E), on average O(1)
        if self.parents[a] != a:
            root = self.findParent(self.parents[a])
            self.parents[a] = root
            return root
        return a

    def merge(self, a, b):
        root_a = self.findParent(a)
        root_b = self.findParent(b)
        self.parents[root_a] = root_b


3
[[1,2,5],[1,3,6],[2,3,1]]

