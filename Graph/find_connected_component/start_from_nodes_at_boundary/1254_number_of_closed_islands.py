#
# public class Q_1254_Number_of_Closed_Islands {
#
#
#    public static void main(String[] args) {
#        Q_1254_Number_of_Closed_Islands solution = new Q_1254_Number_of_Closed_Islands();
#        int[][] grid1 = {{1,1,1,1,1,1,1,0},{1,0,0,0,0,1,1,0},{1,0,1,0,1,1,1,0},{1,0,0,0,0,1,0,1},{1,1,1,1,1,1,1,0}};
#        int[][] grid2 = {{0,0,1,0,0},{0,1,0,1,0},{0,1,1,1,0}};
#        int[][] grid3 = {{1,1,1,1,1,1,1}, {1,0,0,0,0,0,1}, {1,0,1,1,1,0,1}, {1,0,1,0,1,0,1}, {1,0,1,1,1,0,1}, {1,0,0,0,0,0,1}, {1,1,1,1,1,1,1}};
#        System.out.println(solution.closedIsland(grid1));
#        System.out.println(solution.closedIsland(grid2));
#        System.out.println(solution.closedIsland(grid3));
#    }
#
#
#    public int closedIsland(int[][] grid) {
#        if (grid.length == 0 || grid[0].length == 0) {
#            return 0;
#        }
#        int m = grid.length;
#        int n = grid[0].length;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (i == 0 || j == 0 || i == m-1 || j == n-1) {
#                    if (grid[i][j] == 0) {
#                        fill(grid, m, n, i, j);
#                    }
#                }
#            }
#        }
#
#
#        int res = 0;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (grid[i][j] == 0) {
#                    res++;
#                    fill(grid, m, n, i, j);
#                }
#            }
#        }
#        return res;
#    }
#
#
#    private void fill(int[][] grid, int m, int n, int i, int j) {
#        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != 0) {
#            return;
#        }
#        grid[i][j] = 1;
#        for (int[] dir : new int[][]{{1,0},{-1,0},{0,1},{0,-1}}) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            fill(grid, m, n, x, y);
#        }
#    }
# }
