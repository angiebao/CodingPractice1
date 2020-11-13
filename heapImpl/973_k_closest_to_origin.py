import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # pq = []
        # heapq.heapify(pq)
        # d = defaultdict(list)
        # for point in points:
        #     distance = point[0]**2+ point[1]**2
        #     heapq.heappush(pq, distance)
        #     d[distance].append([point[0], point[1]])
        # res = []
        # while K >0:
        #     distance = heapq.heappop(pq)
        #     for v in d[distance]:
        #         res.append(v)
        #         K -= 1
        # return res

        pq = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(pq, (distance, point[0], point[1]))

        res = []
        while K > 0:
            (distance, p1, p2) = heapq.heappop(pq)
            res.append([p1, p2])
            K -= 1
        return res