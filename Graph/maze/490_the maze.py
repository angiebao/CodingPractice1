# #There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
# The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
# When the ball stops, it could choose the next direction.
#
# Given the maze, the ball's start position and the destination, where start = [startrow, startcol] and
# destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
#
# You may assume that the borders of the maze are all walls (see examples).
#
#

#
# public class Q_0490_The_Maze {
#
#
#    public static void main(String[] args) {
#        Q_0490_The_Maze solution = new Q_0490_The_Maze();
#        int[][] maze = {{0,0,1,0,0}, {0,0,0,0,0}, {0,0,0,1,0}, {1,1,0,1,1}, {0,0,0,0,0}};
#        int[] start = {0,4};
#        int[] destination1 = {4,4};
#        int[] destination2 = {3,2};
#        System.out.println(solution.hasPath(maze, start, destination1));
#        System.out.println(solution.hasPath(maze, start, destination2));
#    }
#
#
#    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
#        int m = maze.length;
#        int n = maze[0].length;
#        boolean[][] visited = new boolean[m][n];
#        boolean res = bfs(maze, m, n, start, destination, visited);
#        return res;
#    }
#
#
#    private boolean bfs(int[][] maze, int m, int n, int[] start, int[] destination, boolean[][] visited) {
#        Queue<Coordinate> q = new LinkedList<>();
#        q.offer(new Coordinate(start[0], start[1]));
#        visited[start[0]][start[1]] = true;
#        while (!q.isEmpty()) {
#            Coordinate curr = q.poll();
#            if (curr.x == destination[0] && curr.y == destination[1]) {
#                return true;
#            }
#            for (int[] dir : Util.dirs) {
#                int x = curr.x + dir[0];
#                int y = curr.y + dir[1];
#                while (0 <= x && x < m && 0 <= y && y < n && maze[x][y] == 0) {
#                    x += dir[0];
#                    y += dir[1];
#                }
#                x -= dir[0];
#                y -= dir[1];
#                if (!visited[x][y]) {
#                    visited[x][y] = true;
#                    q.offer(new Coordinate(x, y));
#                }
#            }
#        }
#        return false;
#    }
#
#
#    private static class Coordinate {
#        int x;
#        int y;
#        Coordinate(int x, int y) {
#            this.x = x;
#            this.y = y;
#        }
#    }
# }

# BFS

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])

        visited = [[False for i in range(n)] for j in range(m)]
        res = self.bfs(maze, m, n, start, destination, visited)
        return res

    def bfs(self, maze, m, n, start, destination, visited):
        q = collections.deque()
        q.append((start[0], start[1]))

        visited[start[0]][start[1]] = True

        while q:
            curr = q.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = curr[0] + direction[0]
                y = curr[1] + direction[1]

                while 0 <= x and x < m and 0 <= y < n and maze[x][y] == 0:
                    x += direction[0]
                    y += direction[1]

                x -= direction[0]
                y -= direction[1]

                if not visited[x][y]:
                    visited[x][y] = True
                    q.append((x, y))

        return False

#
import collections
class Solution:
    def hasPath(self, maze, start, destination):

        n, m = len(maze), len(maze[0])
        dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        q = collections.deque()
        visited = set()

        for k in dirs:
            nx, ny = start[0] + k[0], start[1] + k[1]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                q.append((start[0], start[1], k))
                visited.add((start[0], start[1], k))

        while q:
            cur = q.popleft()

            if cur[0] == destination[0] and cur[1] == destination[1]:
                return True

            k = cur[2]
            nx, ny = cur[0] + k[0], cur[1] + k[1]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                if (nx, ny, k) not in visited:
                    q.append((nx, ny, k))
            else:
                for k in dirs:
                    nx, ny = cur[0] + k[0], cur[1] + k[1]
                    if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                        if (cur[0], cur[1], k) not in visited:
                            q.append((cur[0], cur[1], k))
                            visited.add((cur[0], cur[1], k))

        return False






maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]

s= Solution()
print(s.hasPath(maze, start, destination))
