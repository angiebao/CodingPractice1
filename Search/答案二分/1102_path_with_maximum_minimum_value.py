# Given a matrix of integers A with R rows and C columns,
# find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
#
# The score of a path is the minimum value in that path.  F
# or example, the value of the path 8 →  4 →  5 →  9 is 4.
#
# A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions
# (north, east, west, south).

# Input: [[5,4,5],
#         [1,2,6],
#         [7,4,6]]
# Output: 4
# Explanation:
# The path with the maximum score is highlighted in yellow.

# Example 2:
# Input: [[2,2,1,2,2,2],
#         [1,2,2,2,1,2]]
# Output: 2
# Example 3:
#
#
#
# Input: [[3,4,6,3,4],
#         [0,2,1,1,7],
#         [8,8,3,2,7],
#         [3,2,4,9,8],
#         [4,1,2,0,0],
#         [4,6,5,4,3]]
# Output: 3


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        left, right = 0, A[0][0]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check(A, mid):
                left = mid
            else:
                right = mid

        if self.check(A, right):
            return right
        return left

    def check(self, matrix, mid):

        def dfs(grid, x, y, mid):
            if grid[x][y] == -1 or grid[x][y] < mid:
                return
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return True

            grid[x][y] = -1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if nx not in range(len(grid)) or ny not in range(len(grid[0])):
                    continue
                if dfs(grid, nx, ny, mid):
                    return True
            return False

        import copy
        matrix = copy.deepcopy(matrix)
        return dfs(matrix, 0, 0, mid)

# class Solution:
#     def maximumMinimumPath(self, A: List[List[int]]) -> int:

#         left, right = 0, A[0][0]
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if self.can_reach(A, mid):
#                 left = mid
#             else:
#                 right = mid
#         return right if self.can_reach(A, right) else left

#     def can_reach(self, A, score):
#         m, n = len(A), len(A[0])
#         delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

#         import collections

#         queue, visited = collections.deque([(0, 0)]), set([(0, 0)])

#         while queue:
#             i, j = queue.popleft()
#             if i == m - 1 and j == n - 1:
#                 return True
#             for (di, dj) in delta:
#                 ni, nj = i + di, j + dj
#                 if ni not in range(m) or nj not in range(n):
#                     continue
#                 if (ni, nj) in visited or A[ni][nj] < score:
#                     continue
#                 queue.append((ni, nj))
#                 visited.add((ni, nj))
#         return False

# class Solution:
#     def maximumMinimumPath(self, A: List[List[int]]) -> int:

#         m, n = len(A), len(A[0])
#         delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

#         import heapq

#         score = [[0 for j in range(n)] for i in range(m)]

#         max_heap, score[0][0] = [(-A[0][0], 0, 0)], A[0][0]

#         while max_heap:
#             cur_score, i, j = heapq.heappop(max_heap)
#             cur_score = -cur_score
#             for (di, dj) in delta:
#                 ni, nj = i + di, j + dj
#                 if ni not in range(m) or nj not in range(n):
#                     continue
#                 next_score = min(cur_score, A[ni][nj])
#                 if next_score <= score[ni][nj]:
#                     continue
#                 score[ni][nj] = next_score
#                 heapq.heappush(max_heap, (-next_score, ni, nj))
#         return score[m - 1][n - 1]