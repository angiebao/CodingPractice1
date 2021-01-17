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

def numIslands_bfs(self, grid):
    # use breadth first search, search for value 1, if it reaches the boundary,
    # then put a flag that this is not an island
    # time complexity O(M*N) = O(nx*ny), space O(nx ), the worst case senario, there are 2*nx node in queue
    if len(grid) == 0:
        return 0
    nx = len(grid)  # number of rows
    ny = len(grid[0])  # number of columns
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = collections.deque()
    island_count = 0

    for i in range(nx):
        for j in range(ny):
            # print ("index x %d and index y %d" %(i, j))
            if grid[i][j] == '1':
                q.append(Node(i, j))
                grid[i][j] = 0
                island_count += 1

            while (len(q) > 0):
                cur = q.popleft()

                for neighbor in range(4):
                    xi, yi = cur.x + directions[neighbor][0], cur.y + directions[neighbor][1]
                    if xi >= 0 and xi < nx and yi >= 0 and yi < ny and grid[xi][yi] == '1':
                        grid[xi][yi] = 0
                        q.append(Node(xi, yi))

#
#    private void dfs(char[][] grid, int m, int n, int i, int j, boolean[][] visited) {
#        if (i < 0 || j < 0 || i >= m || j >= n || visited[i][j] || grid[i][j] != '1') {
#            return;
#        }
#        visited[i][j] = true;
#        for (int[] dir : Util.dirs) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            dfs(grid, m, n, x, y, visited);
#        }
#    }
# }
