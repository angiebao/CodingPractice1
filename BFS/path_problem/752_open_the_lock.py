import collections


class Node():
    def __init__(self, a, b, c, d, step):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.step = step


class Solution:
    # time 10000, space 10000
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends and target != '0000':
            return -1

        q = collections.deque()
        n = 9
        directions = [(1, 0, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0), (0, 0, -1, 0),
                      (0, 0, 0, 1), (0, 0, 0, -1)]
        q.append(Node(0, 0, 0, 0, 0))
        res = 10001
        visited = set()
        visited.add('0000')
        deadends = set(deadends)

        while len(q) > 0:
            cur = q.popleft()
            # visited.add(str(cur.a)+str(cur.b)+str(cur.c)+str(cur.d))

            for i in range(8):
                ai, bi, ci, di = cur.a + directions[i][0], cur.b + directions[i][1], cur.c + directions[i][2], cur.d + \
                                 directions[i][3]
                if ai < 0:
                    ai = 9
                elif ai > 9:
                    ai = 0

                if bi < 0:
                    bi = 9
                elif bi > 9:
                    bi = 0

                if ci < 0:
                    ci = 9
                elif ci > 9:
                    ci = 0

                if di < 0:
                    di = 9
                elif di > 9:
                    di = 0

                position = str(ai) + str(bi) + str(ci) + str(di)
                if position == target:
                    return cur.step + 1

                if (position not in deadends) and (position not in visited):
                    q.append(Node(ai, bi, ci, di, cur.step + 1))
                    visited.add(position)

        return -1