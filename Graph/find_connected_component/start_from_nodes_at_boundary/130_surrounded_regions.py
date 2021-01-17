# #
# #
#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.

# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# public class Q_0130_Surrounded_Regions {
#
#
#    public static void main(String[] args) {
#        Q_0130_Surrounded_Regions solution = new Q_0130_Surrounded_Regions();
#        char[][] board1 = {{'X','X','X','X'},
#                {'X','O','O','X'},
#                {'X','X','O','X'},
#                {'X','O','X','X'}};
#
#
#        char[][] board2 = {{'O','O','O','O'},
#                {'O','O','O','O'},
#                {'O','O','O','O'},
#                {'O','O','O','O'}};
#
#
#        solution.solve1(board1);
#        Util.printMatrix(board1);
#        System.out.println();
#        solution.solve1(board2);
#        Util.printMatrix(board2);
#        Util.printSeparator();
#        solution.solve2(board1);
#        Util.printMatrix(board1);
#        System.out.println();
#        solution.solve2(board2);
#        Util.printMatrix(board2);
#    }
#
#
#    /*
#        Solution 1: BFS
#     */
#    public void solve1(char[][] board) {
#        if (board.length == 0 || board[0].length == 0) {
#            return;
#        }
#        int m = board.length;
#        int n = board[0].length;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (i == 0 || j == 0 || i == m-1 || j == n-1) {
#                    if (board[i][j] == 'O') {
#                        bfs(board, m, n, i, j);
#                    }
#                }
#            }
#        }
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (board[i][j] == '*') {
#                    board[i][j] = 'O';
#                } else if (board[i][j] == 'O') {
#                    board[i][j] = 'X';
#                }
#            }
#        }
#    }
#
#
#    private void bfs(char[][] board, int m, int n, int i, int j) {
#        Queue<Coordinate> q = new LinkedList<>();
#        q.offer(new Coordinate(i, j));
#        board[i][j] = '*';
#        while (!q.isEmpty()) {
#            Coordinate curr = q.poll();
#            for (int[] dir : new int[][]{{0,1},{0,-1},{1,0},{-1,0}}) {
#                int x = curr.x + dir[0];
#                int y = curr.y + dir[1];
#                if (0 <= x && x < m && 0 <= y && y < n && board[x][y] == 'O') {
#                    board[x][y] = '*';
#                    q.offer(new Coordinate(x, y));
#                }
#            }
#        }
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
#
#
#    /*
#        Solution 2: DFS
#     */
#    public void solve2(char[][] board) {
#        if (board.length == 0 || board[0].length == 0) {
#            return;
#        }
#        int m = board.length;
#        int n = board[0].length;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (i == 0 || j == 0 || i == m-1 || j == n-1) {
#                    dfs(board, m, n, i, j);
#                }
#            }
#        }
#
#
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (board[i][j] == '*') {
#                    board[i][j] = 'O';
#                } else {
#                    board[i][j] = 'X';
#                }
#            }
#        }
#    }
#
#
#    private void dfs(char[][] board, int m, int n, int i, int j) {
#        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != 'O') {
#            return;
#        }
#        board[i][j] = '*';
#        for (int[] dir : new int[][]{{1,0},{-1,0},{0,1},{0,-1}}) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            dfs(board, m, n, x, y);
#        }
#    }
# }


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    self.dfs(board, m, n, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def dfs(self, board, m, n, i, j):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return

        board[i][j] = '*'
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = i + dir[0]
            y = j + dir[1]
            self.dfs(board, m, n, x, y)