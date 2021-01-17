# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
# Example 2:
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# Example 3:
#
# Input: ")("
# Output: [""]

# public class Q_0301_Remove_Invalid_Parentheses {
#
#
#    public static void main(String[] args) {
#        Q_0301_Remove_Invalid_Parentheses solution = new Q_0301_Remove_Invalid_Parentheses();
#        String s1 = "()())()";
#        String s2 = "(a)())()";
#        String s3 = ")(";
#        System.out.println(solution.removeInvalidParentheses(s1));
#        System.out.println(solution.removeInvalidParentheses(s2));
#        System.out.println(solution.removeInvalidParentheses(s3));
#    }
#
#
#    public List<String> removeInvalidParentheses(String s) {
#        List<String> res = new ArrayList<>();
#        bfs(s, res);
#        return res;
#    }
#
#
#    private void bfs(String s, List<String> res) {
#        Queue<String> q = new LinkedList<>();
#        Set<String> visited = new HashSet<>();
#        q.offer(s);
#        visited.add(s);
#        while (!q.isEmpty()) {
#            boolean found = false;
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                String curr = q.poll();
#                if (isvalid(curr)) {
#                    res.add(curr);
#                    found = true;
#                }
#                for (int j = 0; j < curr.length(); j++) {
#                    char c = curr.charAt(j);
#                    if (c == '(' || c == ')') {
#                        String next = curr.substring(0,j) + curr.substring(j+1);
#                        if (visited.add(next)) {
#                            q.offer(next);
#                        }
#                    }
#                }
#            }
#            if (found) break;
#        }
#    }
#
#
#    private boolean isvalid(String s) {
#        int cnt = 0;
#        for (char c : s.toCharArray()) {
#            if (c == '(') {
#                cnt++;
#            } else if (c == ')') {
#                if (cnt == 0) return false;
#                cnt--;
#            }
#        }
#        return cnt == 0;
#    }
# }