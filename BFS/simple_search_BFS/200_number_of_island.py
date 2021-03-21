# can modify existing graph or not.  i*n+j as id to represent each position to record if it is visited
# can use dfs or not, dfs can result in stack overflow problem if the dataset is large

# 200. Number of Islands
# public class Q_0200_Number_of_Islands {
#
#
#    public static void main(String[] args) {
#        Q_0200_Number_of_Islands solution = new Q_0200_Number_of_Islands();
#        char[][] grid1 = {{'1','1','1','1','0'}, {'1','1','0','1','0'}, {'1','1','0','0','0'}, {'0','0','0','0','0'}};
#        char[][] grid2 = {{'1','1','0','0','0'}, {'1','1','0','0','0'}, {'0','0','1','0','0'}, {'0','0','0','1','1'}};
#        System.out.println(solution.numIslands1(grid1));
#        System.out.println(solution.numIslands1(grid2));
#
#
#        System.out.println(solution.numIslands2(grid1));
#        System.out.println(solution.numIslands2(grid2));
#    }
#
#
#    public int numIslands1(char[][] grid) {
#        if (grid.length == 0 || grid[0].length == 0) return 0;
#
#
#        int m = grid.length;
#        int n = grid[0].length;
#        boolean[][] visited = new boolean[m][n];
#        int cnt = 0;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (!visited[i][j] && grid[i][j] == '1') {
#                    cnt++;
#                    bfs(grid, m, n, i, j, visited);
#                }
#            }
#        }
#        return cnt;
#    }
#
#
#    public int numIslands2(char[][] grid) {
#        if (grid.length == 0 || grid[0].length == 0) return 0;
#
#
#        int m = grid.length;
#        int n = grid[0].length;
#        boolean[][] visited = new boolean[m][n];
#        int cnt = 0;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (!visited[i][j] && grid[i][j] == '1') {
#                    cnt++;
#                    dfs(grid, m, n, i, j, visited);
#                }
#            }
#        }
#        return cnt;
#    }
#
#
#    private void bfs(char[][] grid, int m, int n, int i, int j, boolean[][] visited) {
#        Queue<Integer> q = new LinkedList<>();
#        q.offer(i*n+j);
#        visited[i][j] = true;
#        while (!q.isEmpty()) {
#            int curr = q.poll();
#            for (int[] dir : Util.dirs) {
#                int x = curr/n + dir[0];
#                int y = curr%n + dir[1];
#                if (0 <= x && x < m && 0 <= y && y < n && !visited[x][y] && grid[x][y] == '1') {
#                    q.offer(x*n+y);
#                    visited[x][y] = true;
#                }
#            }
#        }
#    }
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        if nr == 0 or nc == 0:
            return 0
        count = 0
        self.grid = grid
        self.visited = [[False for i in range(nc)] for j in range(nr)]

        for i in range(nr):
            for j in range(nc):
                if self.grid[i][j] == '1' and self.visited[i][j] == False:
                    self.visited[i][j] = True
                    self.bfs(i, j, nr, nc)
                    count += 1

        return count

    def bfs(self, i, j, nr, nc):
        q = collections.deque()
        q.append((i, j))

        while q:
            cur = q.popleft()
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = cur[0] + direction[0], cur[1] + direction[1]
                if 0 <= x < nr and 0 <= y < nc and self.grid[x][y] == '1' and not self.visited[x][y]:
                    self.visited[x][y] = True
                    q.append((x, y))


