import collections

class Solution:
    def orangesRotting(self, grid):
        self.R = len(grid)
        self.C = len(grid[0])
        sr, sc = 0, 0
        self.rq, self.cq = collections.deque(), collections.deque()
        self.m = grid

        move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0

        reached_end = False
        self.visited = []
        self.visited.append([])
        self.visited.append([])

        self.dr = [-1, +1, 0, 0]
        self.dc = [0, 0, +1, -1]

        self.rq.append(sr)
        self.cq.append(sc)
        self.visited[sr][sc] = True

        while len(self.rq) > 0:
            r = self.rq.popleft()
            c = self.cq.popleft()
            if self.m[r, c] == 'E':
                reached_end = True
            self.explore_neighbors(r, c)
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
            self.nodes_in_next_layer = 0
            move_count += 1

        if reached_end:
            return move_count

        return -1

    def explore_neighbors(self, r, c):
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
            if self.m == '#':
                continue

            self.rq.append(rr)
            self.cq.append(cc)
            self.visited[rr][cc] = True
            self.nodes_in_next_layer += 1
