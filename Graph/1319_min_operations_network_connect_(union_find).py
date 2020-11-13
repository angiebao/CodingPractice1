# 1319. Number of Operations to Make Network Connected
# Medium
# There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
#
# Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.
#
# Example 1:
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

# Example 2:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2

# Example 3:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.

# Example 4:
# Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
# Output: 0
#
# Constraints:
#
# 1 <= n <= 10^5
# 1 <= connections.length <= min(n*(n-1)/2, 10^5)
# connections[i].length == 2
# 0 <= connections[i][0], connections[i][1] < n
# connections[i][0] != connections[i][1]
# There are no repeated connections.
# No two computers are connected by more than one cable.

import collections


class Solution:
    def makeConnected(self, n: int, connections): #List[List[int]]) -> int:
        self.parents = [i for i in range(n)]

        # graph = collections.defaultdict(list)
        # for (u, v) in connections:
        #     graph[u].append(v)
        #     graph[v].append(u)

        count = 0
        for (u, v) in connections:
            if not self.is_connected(u, v):
                self.merge(u, v)
            else:
                # there is loop exist, cut this line
                count += 1

        groups = {self.find(i) for i in range(n)}

        # 把分散的group 连在一起，loop中砍掉的线够不够？
        if len(groups) - 1 <= count:
            return (len(groups) - 1)
        else:
            return -1

    def find(self, index):
        if self.parents[index] != index:
            root = self.find(self.parents[index])
            self.parents[index] = root
            return root
        return index

    def is_connected(self, index1, index2):
        return self.find(index1) == self.find(index2)

    def merge(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        self.parents[root1] = root2
