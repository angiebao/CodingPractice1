import collections
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # use breadth first search, search for value 1, if it reaches the boundary,
#         # then put a flag that this is not an island
#         #time complexity O(M*N) = O(nx*ny), space O(nx*ny + nx )
#         if len(grid) == 0 :
#             return 0
#         nx = len(grid) # number of rows
#         ny = len(grid[0]) #number of columns
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         q = collections.deque()
#         visited = [[False] * ny for i in range(nx)]
#         island_count = 0

#         for i in range(nx):
#             for j in range(ny):
#                 #print ("index x %d and index y %d" %(i, j))
#                 if grid[i][j] == '1' and visited[i][j] == False:
#                     q.append(Node(i, j))
#                     visited[i][j] = True
#                     island_count += 1

#                 while (len(q) > 0):
#                     cur = q.popleft()

#                     for neighbor in range(4):
#                         xi, yi = cur.x +  [neighbor][0], cur.y + directions[neighbor][1]
#                         if xi >= 0 and xi < nx and yi >= 0 and yi < ny and grid[xi][yi] == '1' and visited[xi][yi]==False:
#                             visited[xi][yi] = True
#                             q.append(Node(xi, yi))



#         return island_count
    def numIslands_bfs(self, grid):
        # use breadth first search, search for value 1, if it reaches the boundary,
        # then put a flag that this is not an island
        #time complexity O(M*N) = O(nx*ny), space O(nx ), the worst case senario, there are 2*nx node in queue
        if len(grid) == 0 :
            return 0
        nx = len(grid) # number of rows
        ny = len(grid[0]) #number of columns
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()
        island_count = 0

        for i in range(nx):
            for j in range(ny):
                #print ("index x %d and index y %d" %(i, j))
                if grid[i][j] == '1' :
                    q.append(Node(i, j))
                    grid[i][j] = 0
                    island_count += 1

                while (len(q) > 0):
                    cur = q.popleft()

                    for neighbor in range(4):
                        xi, yi = cur.x +  directions[neighbor][0], cur.y + directions[neighbor][1]
                        if xi >= 0 and xi < nx and yi >= 0 and yi < ny and grid[xi][yi] == '1' :
                            grid[xi][yi] = 0
                            q.append(Node(xi, yi))



        return island_count

    def numIslands(self, grid):
        self.grid = grid
        self.nr = len(grid)
        self.nc = len(grid[0])
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.visited = [[False]*self.nc for i in range(self.nr)]
        self.island_count = 0
        for i in range(self.nr):
            for j in range(self.nc):
                if self.grid[i][j] == '1' and self.visited[i][j] == False:
                    self.visited[i][j] = True
                    self.dfs(Node(i,j))
                    self.island_count += 1
        return self.island_count

    def dfs(self, cur):
        for i in range(4):
            xi, yi = cur.x + self.directions[i][0], cur.y + self.directions[i][1]
            if xi >= 0 and xi < self.nr and yi >= 0 and yi < self.nc and self.grid[xi][yi] == '1' and self.visited[xi][yi] == False:
                self.visited[xi][yi] = True
                self.dfs(Node(xi, yi))

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"] ]
#grid = [["1", "0"]]
s= Solution()
num =s.numIslands(grid)
print(num)