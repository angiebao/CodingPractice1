# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
#


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nr = len(grid)
        nc = len(grid[0])

        if nr == 0 or nc == 0:
            return 0
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        self.grid = grid

        self.visited = [[False for i in range(nc)] for j in range(nr)]

        maxArea = 0

        for i in range(nr):
            for j in range(nc):
                if self.grid[i][j] == 1 and (not self.visited[i][j]):
                    self.visited[i][j] = True
                    area = self.dfs(nr, nc, (i, j))
                    if area > maxArea:
                        maxArea = area
        return maxArea

    def dfs(self, nr, nc, cur):
        area = 1
        for direction in self.directions:
            xi, yi = cur[0] + direction[0], cur[1] + direction[1]
            if xi >= 0 and xi < nr and yi >= 0 and yi < nc and self.grid[xi][yi] == 1 and not self.visited[xi][yi]:
                self.visited[xi][yi] = True
                area += self.dfs(nr, nc, (xi, yi))
        return area


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#
#         nr = len(grid)
#         nc = len(grid[0])
#
#         if nr ==0 or nc == 0:
#             return 0
#         self.directions = [(1,0),(-1,0),(0, -1),(0, 1)]
#         self.grid = grid
#
#         self.visited = [[False for i in range(nc)] for j in range(nr)]
#
#         maxArea = 0
#
#
#         for i in range(nr):
#             for j in range(nc):
#                 if self.grid[i][j] == 1 and (not self.visited[i][j]):
#                     self.visited[i][j] = True
#                     self.curArea = 1
#                     self.dfs(nr, nc, (i, j))
#                     if self.curArea > maxArea:
#                         maxArea = self.curArea
#
#         return maxArea
#
#
#
#     def dfs(self, nr, nc, cur):
#         for direction in self.directions:
#             xi, yi = cur[0] + direction[0], cur[1] + direction[1]
#             if xi >=0 and xi< nr and yi >=0 and yi< nc and self.grid[xi][yi] == 1 and not self.visited[xi][yi]:
#                 self.visited[xi][yi] = True
#                 self.curArea = self.curArea  + 1
#                 self.dfs(nr, nc, (xi, yi))