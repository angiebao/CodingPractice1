# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
# Input:
# image =
#
# [
# [1,1,1],
# [1,1,0],
# [1,0,1]
# ]
#
# sr = 1, sc = 1, newColor = 2
# Output:
# [
# [2,2,2],
# [2,2,0],
# [2,0,1]
# ]
#
#
#
# [
# [1,2,1],
# [2,2,0],
# [1,0,1]
# ]
# sr = 1, sc = 1, newColor = 2

# public class Q_0733_Flood_Fill {
#
#
#    public static void main(String[] args) {
#        Q_0733_Flood_Fill solution = new Q_0733_Flood_Fill();
#        int[][] image = {{1,1,1},{1,1,0},{1,0,1}};
#        Util.printMatrix(solution.floodFill(image, 1, 1, 2));
#    }
#
#
#    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
#        int m = image.length;
#        int n = image[0].length;
#        dfs(image, m, n, sr, sc, image[sr][sc], newColor, new boolean[m][n]);
#        return image;
#    }
#
#
#    private void dfs(int[][] image, int m, int n, int i, int j, int color, int newColor, boolean[][] visited) {
#        if (i < 0 || j < 0 || i >= m || j >= n || image[i][j] != color || visited[i][j]) {
#            return;
#        }
#        image[i][j] = newColor;
#        visited[i][j] = true;
#        for (int[] dir : new int[][]{{1,0},{-1,0},{0,1},{0,-1}}) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            dfs(image, m, n, x, y, color, newColor, visited);
#        }
#        visited[i][j] = false;
#    }
# }

