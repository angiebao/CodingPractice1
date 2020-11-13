# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?
#
# Example:
#
# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]
#
# Output: 2
#
# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]

class Node():
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step


import collections
def minHours( rows,  columns,  grid):
    deq = collections.deque()

    directions = [(0,1), (1, 0), (0, -1),(-1, 0)]

    # initialize the queue
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                deq.append(Node(i, j, 0))
    res = 0
    while deq:
        cur = deq.popleft()

        for i in range(4):
            r = cur.x + directions[i][0]
            c = cur.y + directions[i][1]
            if r>=0 and r<rows and c >=0 and c< columns and grid[r][c] == 0:
                grid[r][c] = 1
                deq.append(Node(r, c, cur.step+1))
                res = max(res, cur.step + 1)
    return res

grid =  [[0, 1, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0]]

rows = 4
columns = 5
print(minHours(rows, columns, grid))