# path finder :
#找到 所有shortest path,
# 用dfs

# ‌Find shortest path (最短路径及长度)
# BFS: 空间复杂度 O(4^n) exponential order ，, 时间 O(mn)
#
# DFS : 可以降低空间复杂度， 空间复杂度O(mn), 时间复杂度 O(exponential order)， 可以用 pruning
# 找到最短路径之一(BFS)         this problem
# 找到所有最短路径(BFS+DFS) ： world ladder2
# 找到最短路径的长度(BFS)： word ladder
# 返回本身  ： 797


# public class PathFinder {
#
#
#    public static void main(String[] args) {
#        PathFinder solution = new PathFinder();
#        char[][] matrix = {{'L','O','X','O','P'},
#                           {'X','O','O','O','O'},
#                           {'X','O','X','X','O'},
#                           {'O','O','O','O','O'}};
#        System.out.println("One of the shortest paths is: ");
#        System.out.println(solution.findAnyShortestPath(matrix));
#        Util.printSeparator();
#
#
#        System.out.println("All shortest paths are: ");
#        List<List<Coordinate>> res = solution.findAllShortestPaths(matrix);
#        for (List<Coordinate> l : res) {
#            System.out.println(l);
#        }
#        Util.printSeparator();
#
#
#        System.out.println("Shortest Distance is: ");
#        System.out.println(solution.findShortestDistance(matrix));
#    }
#
#
#    // 找到其中一条最短路径(BFS)
#    public List<Coordinate> findAnyShortestPath(char[][] matrix) {
#        int m = matrix.length;
#        int n = matrix[0].length;
#        Coordinate start = new Coordinate(-1,-1);
#        Coordinate dest = new Coordinate(-1,-1);
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (matrix[i][j] == 'L') start = new Coordinate(i, j);
#                if (matrix[i][j] == 'P') dest = new Coordinate(i, j);
#            }
#        }
#        return findAnyShortestPathHelper(matrix, m, n, start, dest);
#    }
#
#
#    // 找到其中所有的最短路径(BFS+DFS)
#    public List<List<Coordinate>> findAllShortestPaths(char[][] matrix) {
#        int m = matrix.length;
#        int n = matrix[0].length;
#        Coordinate start = new Coordinate(-1,-1);
#        Coordinate dest = new Coordinate(-1,-1);
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (matrix[i][j] == 'L') start = new Coordinate(i, j);
#                if (matrix[i][j] == 'P') dest = new Coordinate(i, j);
#            }
#        }
#        List<List<Coordinate>> res = new ArrayList<>();
#        // get shortest distance
#        int dist = findShortestDistanceHelper(matrix, m, n, start, dest);
#        // find all shortest paths using dfs
#        findAllShortestPathsHelper(matrix, m, n, 0, start, dest, dist, new boolean[m][n], new ArrayList<>(), res);
#        return res;
#    }
#
#
#    // 找到最短路径的长度(BFS)
#    public int findShortestDistance(char[][] matrix) {
#        int m = matrix.length;
#        int n = matrix[0].length;
#        Coordinate start = new Coordinate(-1,-1);
#        Coordinate dest = new Coordinate(-1,-1);
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (matrix[i][j] == 'L') start = new Coordinate(i, j);
#                if (matrix[i][j] == 'P') dest = new Coordinate(i, j);
#            }
#        }
#        return findShortestDistanceHelper(matrix, m, n, start, dest);
#    }
#
#
#    private List<Coordinate> findAnyShortestPathHelper(char[][] matrix, int m, int n, Coordinate start, Coordinate dest) {
#        Queue<List<Coordinate>> q = new LinkedList<>();
#        Set<Integer> visited = new HashSet<>();
#        q.offer(Arrays.asList(start));
#        visited.add(start.x * n + start.y);
#
#
#        while (!q.isEmpty()) {
#            List<Coordinate> curr = q.poll();
#            Coordinate last = curr.get(curr.size() - 1);
#            if (last.x == dest.x && last.y == dest.y) {
#                return curr;
#            }
#            for (int[] dir : new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
#                int x = last.x + dir[0];
#                int y = last.y + dir[1];
#                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != 'X' && visited.add(x * n + y)) {
#                    List<Coordinate> next = new ArrayList<>(curr);
#                    next.add(new Coordinate(x, y));
#                    q.offer(next);
#                }
#            }
#        }
#        return new ArrayList<>();
#    }
#
#
#    private int findShortestDistanceHelper(char[][] matrix, int m, int n, Coordinate start, Coordinate dest) {
#        Queue<List<Coordinate>> q = new LinkedList<>();
#        Set<Integer> visited = new HashSet<>();
#        q.offer(Arrays.asList(start));
#        visited.add(start.x * n + start.y);
#        int res = 0;
#
#
#        while (!q.isEmpty()) {
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                List<Coordinate> curr = q.poll();
#                Coordinate last = curr.get(curr.size()-1);
#                if (last.x == dest.x && last.y == dest.y) {
#                    return res;
#                }
#                for (int[] dir : new int[][]{{0,1},{0,-1},{1,0},{-1,0}}) {
#                    int x = last.x + dir[0];
#                    int y = last.y + dir[1];
#                    if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != 'X' && visited.add(x*n + y)) {
#                        List<Coordinate> next = new ArrayList<>(curr);
#                        next.add(new Coordinate(x, y));
#                        q.offer(next);
#                    }
#                }
#            }
#            res++;
#        }
#        return -1;
#    }
#
#
#    private void findAllShortestPathsHelper(char[][] matrix,
#                                            int m,
#                                            int n,
#                                            int d,
#                                            Coordinate curr,
#                                            Coordinate dest,
#                                            int dist,
#                                            boolean[][] visited,
#                                            List<Coordinate> list,
#                                            List<List<Coordinate>> res) {
#        if (d > dist) {
#            return;
#        }
#        list.add(curr);
#        visited[curr.x][curr.y] = true;
#        if (d == dist && curr.x == dest.x && curr.y == dest.y) {
#            res.add(new ArrayList<>(list));
#        } else {
#            for (int[] dir : new int[][]{{0,1},{0,-1},{1,0},{-1,0}}) {
#                int x = curr.x + dir[0];
#                int y = curr.y + dir[1];
#                if (0 <= x && x < m && 0 <= y && y < n && !visited[x][y] && matrix[x][y] != 'X') {
#                    findAllShortestPathsHelper(matrix, m, n, d+1, new Coordinate(x, y), dest, dist, visited, list, res);
#                }
#            }
#        }
#        visited[curr.x][curr.y] = false;
#        list.remove(list.size()-1);
#    }
#
#
#    private static class Coordinate {
#        private int x;
#        private int y;
#        Coordinate(int x, int y) {
#            this.x = x;
#            this.y = y;
#        }
#        @Override
#        public String toString() {
#            return "(" + x + "," + y + ")";
#        }
#    }
# }
