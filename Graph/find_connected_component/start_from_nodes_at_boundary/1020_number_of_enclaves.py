# Input:
# Example 1:
# [
# [0,0,0,0],
# [1,0,1,0],
# [0,1,1,0],
# [0,0,0,0]
# ]
# Return 3.
#
# Example 2
# [
# [0,1,1,0],
# [0,0,1,0],
# [0,0,1,0],
# [0,0,0,0]
# ]
# Return 0
#
# Return the number of 1’s which are not connected to the boundary


# public class Q_1020_Number_of_Enclaves {
#
#
#    public static void main(String[] args) {
#        Q_1020_Number_of_Enclaves solution = new Q_1020_Number_of_Enclaves();
#        int[][] A1 = {{0,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,0}};
#        int[][] A2 = {{0,1,1,0},{0,0,1,0},{0,0,1,0},{0,0,0,0}};
#        System.out.println(solution.numEnclaves(A1));
#        System.out.println(solution.numEnclaves(A2));
#    }
#
#
#    public int numEnclaves(int[][] A) {
#        if (A.length == 0 || A[0].length == 0) {
#            return 0;
#        }
#        int m = A.length;
#        int n = A[0].length;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (i == 0 || j == 0 || i == m-1 || j == n-1) {
#                    if (A[i][j] == 1) {
#                        dfs(A, m, n, i, j);
#                    }
#                }
#            }
#        }
#
#
#        int res = 0;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (A[i][j] == 1) {
#                    res++;
#                }
#            }
#        }
#        return res;
#    }
#
#
#    private void dfs(int[][] A, int m, int n, int i, int j) {
#        if (i < 0 || j < 0 || i >= m || j >= n || A[i][j] != 1) {
#            return;
#        }
#        A[i][j] = -1;
#        for (int[] dir : new int[][]{{1,0},{-1,0},{0,1},{0,-1}}) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            dfs(A, m, n, x, y);
#        }
#    }
# }
