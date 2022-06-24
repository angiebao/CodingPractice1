# public class Q_0079_Word_Search {
#
#
#    public static void main(String[] args) {
#        Q_0079_Word_Search solution = new Q_0079_Word_Search();
#        char[][] board1 = {{'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'}};
#        String word1 = "ABCCED";
#        String word2 = "SEE";
#        String word3 = "ABCB";
#        System.out.println(solution.exist(board1, word1));
#        System.out.println(solution.exist(board1, word2));
#        System.out.println(solution.exist(board1, word3));
#
#
#        char[][] board2 = {{'a'}};
#        String word4 = "a";
#        System.out.println(solution.exist(board2, word4));
#    }
#
#
#    public boolean exist(char[][] board, String word) {
#        int m = board.length;
#        int n = board[0].length;
#        for (int i = 0; i < m; i++) {
#            for (int j = 0; j < n; j++) {
#                if (dfs(board, m, n, i, j, 0, word)) {
#                    return true;
#                }
#            }
#        }
#        return false;
#    }
#
#
#    private boolean dfs(char[][] board, int m, int n, int i, int j, int index, String word) {
#        if (index == word.length()) return true;
#        if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] != word.charAt(index)) return false;
#        board[i][j] = '*';
#
#
#        boolean exist = false;
#        for (int[] dir : new int[][]{{1,0},{-1,0},{0,1},{0,-1}}) {
#            int x = i + dir[0];
#            int y = j + dir[1];
#            exist |= dfs(board, m, n, x, y, index + 1, word);
#            if (exist) break;
#        }
#        board[i][j] = word.charAt(index);
#        return exist;
#    }
# }

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.nr = len(board)
        self.nc = len(board[0])
        exit = False
        self.visited = [[False for i in range(self.nc)] for j in range(self.nr)]

        for i in range(self.nr):
            for j in range(self.nc):
                curr = board[i][j]
                index = (i, j)
                self.visited[i][j] = True
                exist = self.dfs(board, index, curr, word)
                self.visited[i][j] = False
                if exist:
                    return True
        return False

    def dfs(self, board, index, curr, word):

        if len(curr) == len(word):
            if curr == word:
                return True
            else:
                return False
                '
        exist = False
        # go through the neighbors
        for direction in self.directions:
            nx = index[0] + direction[0]
            ny = index[1] + direction[1]
            if 0 <= nx < self.nr and 0 <= ny < self.nc and not self.visited[nx][ny] and curr == word[:len(curr)]:
                self.visited[nx][ny] = True
                exist = self.dfs(board, (nx, ny), curr + board[nx][ny], word)
                if exist:
                    break
                self.visited[nx][ny] = False
        # in last layer if cannot find any in the neighbor, return False
        return exist
