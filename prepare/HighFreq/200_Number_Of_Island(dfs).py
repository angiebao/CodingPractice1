import collections


class Solution(object):
    def numIslands(self, grid):
        self.r = len(grid)
        if self.r == 0:
            return 0
        self.c = len(grid[0])
        self.visited = [[0 for j in range(self.c)] for i in range(self.r)]
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        self.grid = grid
        num_island = 0
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == '1':
                    self.dfs(i, j)
                    num_island += 1
        return num_island

    def dfs(self, i, j):
        for direction in self.directions:
            x = i + direction[0]
            y = j + direction[1]
            if 0 <= x < self.r and 0 <= y < self.c and self.grid[x][y] == '1':
                self.grid[x][y] = '0'
                self.dfs(x, y)

#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         r = len(grid)
#         if r ==0:
#             return 0
#         c = len(grid[0])
#         q = collections.deque()
#         directions = [(0,1),(-1,0),(0,-1),(1,0)]
#         num_island = 0
#         # put all the 1's in the queue

#         for i in range(r):
#             for j in range(c):
#                 # append the value of grid = 1 to the queue
#                 if grid[i][j] == '1':
#                     q.append((i,j))
#                     grid[i][j] = '0'
#                     num_island += 1

#                 # bfs through the neighbors
#                 while len(q)>0:
#                     cur = q.popleft()
#                     for direction in directions:
#                         x = cur[0] + direction[0]
#                         y = cur[1] + direction[1]

#                         if 0<=x<r and 0<=y<c  and grid[x][y] == '1':
#                             q.append((x,y))
#                             grid[x][y] = '0'


#         return num_island