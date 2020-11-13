import collections


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def solve_bfs(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # method 1 use breadth first, check if any O is on bounary
        # method 2 use bfs, but start with the boundary o and mark the ajacncy grid to be visited, then
        # turn the rest o to be x, time O(M*M) , space O(NR*NC +NR)=O(nr*nc)
        if len(board) == 0:
            return board

        nr = len(board)
        nc = len(board[0])
        visited = [[False] * nc for i in range(nr)]
        q = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if nr <= 2 or nc <= 2:
            return board

        for j in [0, nc - 1]:
            for i in range(nr):
                if board[i][j] == 'O':
                    q.append(Node(i, j))
        for i in [0, nr - 1]:
            for j in range(1, nc - 1):
                if board[i][j] == 'O':
                    q.append(Node(i, j))

        while len(q) > 0:
            cur = q.popleft()
            visited[cur.x][cur.y] = True
            for i in range(4):
                xi, yi = cur.x + directions[i][0], cur.y + directions[i][1]
                if xi < nr and xi >= 0 and yi < nc and yi >= 0 and board[xi][yi] == 'O' and visited[xi][yi] == False:
                    visited[xi][yi] = True
                    q.append(Node(xi, yi))

        for i in range(1, nr - 1):
            for j in range(1, nc - 1):
                if visited[i][j] == False and board[i][j] == 'O':
                    board[i][j] = 'X'

    def solve_dfs(self, board):
        if len(board) == 0:
            return board

        self.nr = len(board)
        self.nc = len(board[0])
        #self.visited = [[False] * self.nc for i in range(self.nr)]
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if self.nr <= 2 or self.nc <= 2:
            return board

        self.board = board

        q = []
        for j in [0, self.nc - 1]:
            for i in range(self.nr):
                if board[i][j] == 'O':
                    q.append(Node(i, j))
        for i in [0, self.nr - 1]:
            for j in range(1, self.nc - 1):
                if board[i][j] == 'O':
                    q.append(Node(i, j))

        for cur in q:
            self.board[cur.x][cur.y] = 'E'
            self.dfs(Node(cur.x, cur.y))

        for i in range(0, self.nr):
            for j in range(0, self.nc):
                if self.board[i][j] == 'E':
                    self.board[i][j] = 'O'
                elif board[i][j] == 'O':
                    self.board[i][j] = 'X'

        board = self.board

    def dfs(self, cur):
        for i in range(4):
            xi, yi = cur.x + self.directions[i][0], cur.y + self.directions[i][1]
            # if xi >= 0 and xi < self.nr and yi >= 0 and yi < self.nc and self.board[xi][yi] != 'O':
            #     return
            if xi >= 0 and xi < self.nr and yi >= 0 and yi < self.nc and self.board[xi][yi] == 'O':
                self.board[xi][yi] = 'E'
                self.dfs(Node(xi, yi))



board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
print(board)
s= Solution()
s.solve_bfs(board)
print(board)
s.solve_dfs(board)
print(board)