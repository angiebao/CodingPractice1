#
# public class Q_0797_All_Paths_From_Source_to_Target {
#
#
#    public static void main(String[] args) {
#        Q_0797_All_Paths_From_Source_to_Target solution = new Q_0797_All_Paths_From_Source_to_Target();
#        int[][] graph = {{1,2}, {3}, {3}, {}};
#        Util.printListOfListInteger(solution.allPathsSourceTarget1(graph));
#        Util.printListOfListInteger(solution.allPathsSourceTarget2(graph));
#    }
#
#
#    /*
#    Solution 1: BFS
#     */
#    public List<List<Integer>> allPathsSourceTarget1(int[][] graph) {
#        List<List<Integer>> res = new ArrayList<>();
#        Queue<List<Integer>> q = new LinkedList<>();
#        q.offer(Arrays.asList(0));
#
#
#        while (!q.isEmpty()) {
#            List<Integer> curr = q.poll();
#            if (curr.get(curr.size()-1) == graph.length-1) {
#                res.add(curr);
#            } else {
#                for (int n : graph[curr.get(curr.size()-1)]) {
#                    List<Integer> next = new ArrayList<>(curr);
#                    next.add(n);
#                    q.offer(next);
#                }
#            }
#        }
#        return res;
#    }
#
#
#    /*
#    Solution 2: DFS
#     */
#    public List<List<Integer>> allPathsSourceTarget2(int[][] graph) {
#        List<List<Integer>> res = new ArrayList<>();
#        dfs(graph, 0, new ArrayList<>(), res);
#        return res;
#    }
#
#
#    private void dfs(int[][] graph, int curr, List<Integer> list, List<List<Integer>> res) {
#        list.add(curr);
#        if (curr == graph.length - 1) {
#            res.add(new ArrayList<>(list));
#        } else {
#            for (int next : graph[curr]) {
#                dfs(graph, next, list, res);
#            }
#        }
#        list.remove(list.size()-1);
#    }
# }

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
#
#
#  0->1
   |
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


# BFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append([0])
        length = len(graph)

        while q:
            curr = q.popleft()
            # when last node in curr == the node n-1, then we found a path
            if curr[len(curr) - 1] == length - 1:
                res.append(curr)
            else:
                # otherwise starting from the last node in curr, keep exploring the last node's neighbor
                for n in graph[curr[len(curr) - 1]]:
                    nxt = curr.copy()
                    nxt.append(n)
                    q.append(nxt)

        return res

