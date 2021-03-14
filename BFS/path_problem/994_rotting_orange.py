# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.




import collections
class Node():
    def __init__(self, x=0, y=0, step=0):
        self.x = x
        self.y = y
        self.step = step

class Solution:
    def orangesRotting(self, grid):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = collections.deque()
        #add initial rotting tomato
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append(Node(i, j, 0))
        res = 0 # store the result of move step
        while (len(q)>0):
            cur = q.popleft()
            for i in range(4): # explore neighbor in four directions
                nx, ny = cur.x + directions[i][0], cur.y + directions[i][1]
                #needless to check grid[nx][ny]==2, because if ==2, it means the grid is visited
                if nx>=0 and nx < n  and ny>=0 and ny < m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append(Node(nx, ny, cur.step+1))
                    res = max(res, cur.step + 1)

        for i in range(n):
            if 1 in grid[i][:]: # check if there is still 1 in gird
                return -1

        return res





    def orangesRotting_2queue(self, grid):
        self.R = len(grid)
        self.C = len(grid[0])

        self.rq, self.cq = collections.deque(), collections.deque()
        self.g = grid

        move_count = 0
        self.nodes_left_in_layer = 0
        self.nodes_in_next_layer = 0

        self.visited = [[False] * self.C for i in range(0, self.R)]

        self.dr = [-1, +1, 0, 0]
        self.dc = [0, 0, +1, -1]

        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == 2:
                    self.nodes_left_in_layer += 1
                    self.rq.append(r)
                    self.cq.append(c)
                    self.visited[r][c] = True

        while (len(self.rq) > 0):
            r = self.rq.popleft()
            c = self.cq.popleft()

            self.explore_neighbors(r, c)
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                move_count += 1

        for i in range(0, self.R):
            for j in range(0, self.C):
                if self.g[i][j] == 1:
                    return -1

        if move_count - 1 < 0:
            return 0
        return move_count - 1

    def explore_neighbors(self, r, c):
        rotted = False
        if self.g[r][c] == 2:
            rotted = True
        for i in range(0, 4):
            rr = r + self.dr[i]
            cc = c + self.dc[i]

            # skip out of bounds locations
            if rr < 0 or cc < 0:
                continue
            if rr >= self.R or cc >= self.C:
                continue
            # skip visited cells
            if self.visited[rr][cc]:
                continue
            if self.g[rr][cc] == 0:
                continue

            self.rq.append(rr)
            self.cq.append(cc)
            self.visited[rr][cc] = True
            self.nodes_in_next_layer += 1
            if rotted:
                self.g[rr][cc] = 2


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[1,1,1,0],[1,1,0,1],[1,0,2,1],[1,1,1,0]]
s = Solution()
move_count = s.orangesRotting(grid)
print(move_count)