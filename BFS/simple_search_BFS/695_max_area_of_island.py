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
# [[1,1,0,0,0],
#  [1,1,0,0,0],
#  [0,0,0,1,1],
#  [0,0,0,1,1]]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nr = len(grid)
        nc = len(grid[0])
        if nr == 0 or nc == 0:
            return 0
        count = 0
        maxArea = 0
        self.grid = grid
        self.visited = [[False for i in range(nc)] for j in range(nr)]

        for i in range(nr):
            for j in range(nc):
                if self.grid[i][j] == 1 and self.visited[i][j] == False:
                    self.visited[i][j] = True
                    area = self.bfs(i, j, nr, nc)
                    if area > maxArea:
                        maxArea = area
        return maxArea

    def bfs(self, i, j, nr, nc):
        q = collections.deque()
        q.append((i, j))
        area = 1
        while q:
            cur = q.popleft()
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = cur[0] + direction[0], cur[1] + direction[1]
                if 0 <= x < nr and 0 <= y < nc and self.grid[x][y] == 1 and not self.visited[x][y]:
                    self.visited[x][y] = True
                    q.append((x, y))
                    area += 1

        return area

