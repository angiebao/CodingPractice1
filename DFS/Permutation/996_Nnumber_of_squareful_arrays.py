





#    public static void main(String[] args) {
#        Q_0996_Number_of_Squareful_Arrays solution = new Q_0996_Number_of_Squareful_Arrays();
#        int[] A1 = {1,17,8};
#        int[] A2 = {2,2,2};
#        System.out.println(solution.numSquarefulPerms(A1));
#        System.out.println(solution.numSquarefulPerms(A2));
#    }
#
#
#    // clarification:
#    // 1. non-negative integers
#    // 2. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
#    public int numSquarefulPerms(int[] A) {
#        Arrays.sort(A); // sort so same numbers will be next to each other
#        int[] cnt = new int[1];
#        helper(A, -1, 0, new boolean[A.length], cnt); // non-negative input so can use -1 as a starter
#        return cnt[0];
#    }
#
#
#    private void helper(int[] A, int last, int index, boolean[] visited, int[] cnt) {
#        if (index == A.length) {
#            cnt[0]++;
#            return;
#        }
#        for (int i = 0; i < A.length; i++) {
#            // is valid candidate if
#            // 1. it's first number
#            // 2. sum of current number and last number is squareful
#            if (last == -1 || (!visited[i] && isSquareful(A[i], last))) {
#                visited[i] = true;
#                helper(A, A[i], index+1, visited, cnt);
#                visited[i] = false;
#                while (i+1 < A.length && A[i] == A[i+1]) i++;
#            }
#        }
#    }
#
#
#    private boolean isSquareful(int first, int second) {
#        double val = Math.sqrt(first + second);
#        return val == Math.floor(val);
#    }
# }

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.count = 0
        self.n = len(A)
        A.sort()
        cur = []
        self.res = []
        visited = [False for i in range(self.n)]
        self.helper(A, cur, visited)
        return len(self.res)

    def helper(self, A, cur, visited):
        if len(cur) == len(A):
            self.res.append(cur[:])
            return

        itr = iter(range(self.n))
        for i in itr:

            if len(cur) == 0 or (not visited[i] and self.isValid(cur[-1], A[i])):
                visited[i] = True
                cur.append(A[i])
                self.helper(A, cur, visited)
                cur.pop()
                visited[i] = False
                while i + 1 < self.n and A[i + 1] == A[i]:
                    i += 1
                    next(itr)

    def isValid(self, x, y):

        z = math.sqrt(x + y)
        return z == math.floor(z)