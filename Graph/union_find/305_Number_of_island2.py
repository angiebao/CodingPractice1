# Union find主要用于实时的 (incremental)
# 找到连通件(connected components)的个数
# 判断是否有环(Cycle)
# 相对于DFS在实时(incremental)的情况下有更优的时间复杂度

# 实时的找到连通件的个数
# ‌时间复杂度O(k) -> k是positions的个数
# public class Q_0305_Number_of_Islands_II {
#
#
#    public static void main(String[] args) {
#        Q_0305_Number_of_Islands_II solution = new Q_0305_Number_of_Islands_II();
#        int m1 = 3;
#        int n1 = 3;
#        int[][] positions1 = {{0,0},{0,1},{1,2},{2,1}};
#
#
#        int m2 = 3;
#        int n2 = 3;
#        int[][] positions2 = {{0,1},{1,2},{2,1},{1,0},{0,2},{0,0},{1,1}};
#
#
#        int m3 = 8;
#        int n3 = 4;
#        int[][] positions3 = {{0,0},{7,1},{6,1},{3,3},{4,1}};
#
#        System.out.println(solution.numIslands2(m1, n1, positions1));
#        System.out.println(solution.numIslands2(m2, n2, positions2));
#        System.out.println(solution.numIslands2(m3, n3, positions3));
#
#
#    }
#
#
#    public List<Integer> numIslands2(int m, int n, int[][] positions) {
#        List<Integer> res = new ArrayList<>();
#        boolean[][] exist = new boolean[m][n];
#        UF uf = new UF(m*n);
#        for (int[] p : positions) {
#            if (!exist[p[0]][p[1]]) {
#                exist[p[0]][p[1]] = true;
#                uf.cnt++; // a new land added
#                for (int[] dir : new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}) {
#                    int x = p[0] + dir[0];
#                    int y = p[1] + dir[1];
#                    if (0 <= x && x < m && 0 <= y && y < n && exist[x][y]) {
#                        uf.union(p[0] * n + p[1], x * n + y);
#                    }
#                }
#            }
#            res.add(uf.cnt);
#        }
#        return res;
#    }
#
#
#    private static class UF {
#        int n;
#        int[] parent;
#        int cnt;
#        UF(int n) {
#            this.n = n;
#            this.cnt = 0;
#            parent = new int[n];
#            for (int i = 0; i < n; i++) {
#                parent[i] = i;
#            }
#        }
#
#
#        int find(int p) {
#            while (p != parent[p]) {
#                p = parent[p];
#                parent[p] = parent[parent[p]];
#            }
#            return p;
#        }
#
#
#        void union(int p, int q) {
#            int rp = find(p);
#            int rq = find(q);
#            if (rp == rq) return;
#            parent[rq] = rp;
#            cnt--;
#        }
#    }
# }