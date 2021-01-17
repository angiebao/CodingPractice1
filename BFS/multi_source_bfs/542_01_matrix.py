
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]


# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# public class Q_0542_01_Matrix {
#
#
#    public static void main(String[] args) {
#        Q_0542_01_Matrix solution = new Q_0542_01_Matrix();
#        int[][] matrix1 = {{0,0,0},{0,1,0},{0,0,0}};
#        int[][] matrix2 = {{0,0,0},{0,1,0},{1,1,1}};
#        Util.printMatrix(solution.updateMatrix(matrix1));
#        Util.printSeparator();
#        Util.printMatrix(solution.updateMatrix(matrix2));
#    }
#
#    public int[][] updateMatrix(int[][] matrix) {
#        int m = matrix.length;
#        int n = matrix[0].length;
#        Queue<Tuple> q = new LinkedList<>();
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (matrix[i][j] == 0) {
#                    q.offer(new Tuple(i, j, 0));
#                } else {
#                    matrix[i][j] = Integer.MAX_VALUE;
#                }
#            }
#        }
#
#
#        while (!q.isEmpty()) {
#            Tuple curr = q.poll();
#            for (int[] dir : new int[][]{{0,1},{0,-1},{1,0},{-1,0}}) {
#                int x = curr.x + dir[0];
#                int y = curr.y + dir[1];
#                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] > curr.d + 1) {
#                    matrix[x][y] = curr.d + 1;
#                    q.offer(new Tuple(x, y, matrix[x][y]));
#                }
#            }
#        }
#        return matrix;
#    }
#
#
#    private class Tuple {
#        private int x;
#        private int y;
#        private int d;
#        Tuple(int x, int y, int d) {
#            this.x = x;
#            this.y = y;
#            this.d = d;
#        }
#    }
# }

# can I modify the existing matrix


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # store x, y, distance information
                    q.append((i, j, 0))
                else:
                    matrix[i][j] = float('inf')
        while q:
            curr = q.popleft()
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = curr[0] + direction[0]
                y = curr[1] + direction[1]
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > curr[2] + 1:
                    matrix[x][y] = curr[2] + 1
                    q.append((x, y, matrix[x][y]))

        return matrix
