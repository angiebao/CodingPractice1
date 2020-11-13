import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        # Time O(E + VlogV)
        # Space O()
        graph = collections.defaultdict(list)

        for (u, v, wt) in flights:
            graph[u].append((v, wt))
            # graph[v].append((u, wt)) # not two directional, only one direction

        pq = [(0, 0, src)]  # when the destination is from src to src, the cost is 0, k = 0, (cost, k, destination)
        best = {}
        while pq:
            (cost, k, place) = heapq.heappop(pq)

            if k > K + 1 or cost > best.get((k, place), float('inf')):
                continue  # go another path

            if place == dst:
                return cost  # best[(k, place)]

            for (neighbor, wt) in graph[place]:
                newcost = cost + wt
                if newcost < best.get((k + 1, neighbor), float('inf')):  # method to initialize dictionary
                    heapq.heappush(pq, (newcost, k + 1, neighbor))
                    best[k + 1, neighbor] = newcost

        return -1

N= 5
flight = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1

s= Solution()
print(s.findCheapestPrice(N, flight, src, dst, k))