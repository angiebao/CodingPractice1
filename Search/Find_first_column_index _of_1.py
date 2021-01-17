#面经如下：1. 一个二维矩阵，里面的数只有0和1，每一行如果有一个1， 那么这行之后的数都是1，
#然后问你对于这个二维矩阵第一个是1的column. binary search 做。楼主漏了一个edge case就是都是0的情况我仍然返回了第一列
# public class FirstColumnWithOne {
#
#    public static void main(String[] args) {
#        FirstColumnWithOne solution = new FirstColumnWithOne();
#        int[][] matrix1 = {{0,0,1,1,1},{0,0,0,1,1}}; // => 2
#        int[][] matrix2 = {{0,0,0,0},{0,0,0,1}};     // => 3
#        int[][] matrix3 = {{0,0}};                   // => -1
#        int[][] matrix4 = {{1,1,1},{0,1,1}};         // => 0
#        System.out.println("1. res: " + solution.getFirstColumnWithOne(matrix1));
#        System.out.println("2. res: " + solution.getFirstColumnWithOne(matrix2));
#        System.out.println("3. res: " + solution.getFirstColumnWithOne(matrix3));
#        System.out.println("4. res: " + solution.getFirstColumnWithOne(matrix4));
#    }
#
#    private int getFirstColumnWithOne(int[][] matrix) {
#        int res = Integer.MAX_VALUE;
#        int len = matrix[0].length;
#        for (int[] A : matrix) {
#            int col = getFirstIndexOfOne(A, len);
#            if (col != -1) {
#                res = Math.min(res, col);
#                len = res+1;
#            }
#        }
#        return res == Integer.MAX_VALUE ? -1 : res;
#    }
#
#    private int getFirstIndexOfOne(int[] A, int len) {
#        int lo = 0;
#        int hi = len-1;
#        while (lo+1<hi) {
#            int mid = lo+(hi-lo)/2;
#            if (A[mid] == 1) {
#                hi = mid;
#            } else {
#                lo = mid;
#            }
#        }
#        if (A[lo] == 1) return lo;
#        else if (A[hi] == 1) return hi;
#        else return -1;
#    }
# }