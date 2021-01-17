# minheap: when pop, we will get the smallest value. In this problem, is the shortest
# maxheap: when pop, we will get the largest value. In this problem, is the longest.
#
# In python, heapq is implemented as minheap. Therefore, if we pop, we will get the smallest number which we don't want, we want to keep the smallest values to return later.
# TutleShip used a trick by adding negative so the largest number becomes smallest so we can use minheap as is. [1,999] -> [-1,-999]

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

# 用 最小堆， 小的在上面， pop 最小值， 找最小的distance， 所以加一个负号在list上， 这样可以pop最大的负值

# heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap.
# The combined action runs more efficiently than heappush() followed by a separate call to heappop().
    def kClosest_diiscussion(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappop(heap)
                heapq.heappush(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]

    kClosest_diiscussion