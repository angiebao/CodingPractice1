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