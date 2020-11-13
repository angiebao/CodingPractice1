# matrix 是岛屿，其中每个cell数表示高度，给定其中一个点表示喷泉，求流水（上下左右4个方向）到海洋(左/右)的最短dist，如图：
#
#                              inf height
#
# ocean（height 0）            1 2  8 4      ocean（height 0）
#                              5 6 7 8
#                              1 2 8 4
#
#                              inf height
# in above, from M[1][2] = 7 , path is 7->6->5 , dist = 3


import collections
def flowdist(M, x, y):
    q = collections.deque()
    q.append((x, y, 0)) # coordinate and dist
    directions = [(0,1),(0,-1),(1,0),(-1,0) ]
    r = len(M)
    c = len(M[0])
    visited = [[0 for i in range(c)] for j in range(r)]
    result = []
    while len(q)>0:
        cur = q.popleft()
        if cur[0] == 0 or cur[1] == c - 1:
            return cur[2] + 1
            #result.append(cur[2] + 1)
        for direction in directions:
            i, j  = cur[0] + direction[0], cur[1] + direction[1]
            if 0<= i < r and 0<= j < c and visited[i][j] == 0 and M[i][j] < M[cur[0]][cur[1]]:
                q.append((i, j, cur[2] + 1))
                visited[i][j] = 1


    #return min(result)

M = [[1,2,8,4], [5,6,7,8] ,[1,2,8,4]]
print(flowdist(M, 1, 2))


