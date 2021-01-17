class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if len(A) == 0:
            return 0
        nr = len(A)
        nc = len(A[0])

        def findFirst():
            for i in range(nr):
                for j in range(nc):
                    if A[i][j]:
                        return i, j

        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            # use A[i][j] = -1 to serve a visited record
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < nr and 0 <= y < nc and A[x][y] == 1:
                    dfs(x, y)

        startx, starty = findFirst()
        bfs = []
        step = 0
        dfs(startx, starty)

        while bfs:
            new = []
            for cur in bfs:
                for (xi, yi) in [(cur[0] + 1, cur[1]), (cur[0] - 1, cur[1]), (cur[0], cur[1] + 1),
                                 (cur[0], cur[1] - 1)]:
                    if 0 <= xi < nr and 0 <= yi < nc:
                        if A[xi][yi] == 1:
                            return step
                        elif A[xi][yi] == 0:
                            A[xi][yi] = -1
                            new.append((xi, yi))

            step += 1
            bfs = new

