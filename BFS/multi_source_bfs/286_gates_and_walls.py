# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

# output:
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.
#
# Example:
#
# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# public class Q_0286_Walls_and_Gates {
#
#
#    public static void main(String[] args) {
#        Q_0286_Walls_and_Gates solution = new Q_0286_Walls_and_Gates();
#        int[][] rooms =
#                {{Integer.MAX_VALUE,-1,0,Integer.MAX_VALUE},
#                {Integer.MAX_VALUE,Integer.MAX_VALUE,Integer.MAX_VALUE,-1},
#                {Integer.MAX_VALUE,-1,Integer.MAX_VALUE ,-1},
#                {0 ,-1,Integer.MAX_VALUE,Integer.MAX_VALUE}};
#        solution.wallsAndGates(rooms);
#        Util.printMatrix(rooms);
#    }
#
#
#    public void wallsAndGates(int[][] rooms) {
#        if (rooms == null || rooms.length == 0 || rooms[0].length == 0) {
#            return;
#        }
#        int m = rooms.length;
#        int n = rooms[0].length;
#        Queue<Tuple> q = new LinkedList<>();
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (rooms[i][j] == 0) {
#                    q.offer(new Tuple(i, j, 0));
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
#                if (0 <= x && x < m && 0 <= y && y < n && rooms[x][y] > curr.d + 1) {
#                    rooms[x][y] = curr.d + 1;
#                    q.offer(new Tuple(x, y, rooms[x][y]));
#                }
#            }
#        }
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

sys.maxsize













