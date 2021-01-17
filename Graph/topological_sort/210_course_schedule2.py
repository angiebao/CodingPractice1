# There are a total of n courses you have to take labelled from 0 to n - 1.
#
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
#
# Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

# public class Q_0210_Course_Schedule_II {
#
#
#    public static void main(String[] args) {
#        Q_0210_Course_Schedule_II solution = new Q_0210_Course_Schedule_II();
#        int numCourses1 = 2;
#        int[][] prerequisites1 = {{1,0}};
#        int numCourses2 = 4;
#        int[][] prerequisites2 = {{1,0}, {2,0}, {3,1}, {3,2}};
#        System.out.println(Arrays.toString(solution.findOrder1(numCourses1, prerequisites1)));
#        System.out.println(Arrays.toString(solution.findOrder1(numCourses2, prerequisites2)));
#        Util.printSeparator();
#        System.out.println(Arrays.toString(solution.findOrder2(numCourses1, prerequisites1)));
#        System.out.println(Arrays.toString(solution.findOrder2(numCourses2, prerequisites2)));
#    }
#
#
#
#
#    // solution 1 (bfs)
#    public int[] findOrder1(int numCourses, int[][] prerequisites) {
#        Map<Integer, Set<Integer>> map = new HashMap<>();
#        int[] ins = new int[numCourses];
#        Queue<Integer> q = new LinkedList<>();
#        init(numCourses, prerequisites, map, ins);
#
#
#        for (int i = 0; i < numCourses; i++) {
#            if (ins[i] == 0) {
#                q.offer(i);
#            }
#        }
#
#
#        List<Integer> list = new ArrayList<>();
#        while (!q.isEmpty()) {
#            int curr = q.poll();
#            list.add(curr);
#            for (int next : map.get(curr)) {
#                if (--ins[next] == 0) {
#                    q.offer(next);
#                }
#            }
#        }
#
#
#        if (list.size() < numCourses) {
#            return new int[0];
#        } else {
#            int[] res = new int[list.size()];
#            for (int i = 0; i < list.size(); i++) {
#                res[i] = list.get(i);
#            }
#            return res;
#        }
#    }
#
#
#    private void init(int n, int[][] A, Map<Integer, Set<Integer>> map, int[] ins) {
#        for (int i = 0; i < n; i++) {
#            map.putIfAbsent(i, new HashSet<>());
#        }
#        for (int[] a : A) {
#            int u = a[0];
#            int v = a[1];
#            if (map.get(v).add(u)) {
#                ins[u]++;
#            }
#        }
#    }
#
#
#    // solution 2 (dfs)
#    public int[] findOrder2(int numCourses, int[][] prerequisites) {
#        Map<Integer, Set<Integer>> map = new HashMap<>();
#        init(numCourses, map, prerequisites);
#        int[] visited = new int[numCourses];
#        Stack<Integer> stack = new Stack<>();
#        for (int i = 0; i < numCourses; i++) {
#            if (visited[i] == 0 && !dfs(i, map, visited, stack)) {
#                return new int[0];
#            }
#        }
#
#
#        // no cycle
#        List<Integer> list = new ArrayList<>();
#        while (!stack.isEmpty()) {
#            list.add(stack.pop());
#        }
#        return list.stream().mapToInt(i->i).toArray();
#    }
#
#
#    private boolean dfs(int curr, Map<Integer, Set<Integer>> map, int[] visited, Stack<Integer> stack) {
#        // visited = 1 -> visiting
#        // visited = 0 -> not visited
#        // visited = 2 -> visited
#        visited[curr] = 1;
#        for (int next : map.get(curr)) {
#            if (visited[next] == 2) continue;
#            if (visited[next] == 1) return false;
#            if (!dfs(next, map, visited, stack)) return false;
#        }
#        visited[curr] = 2;
#        stack.push(curr);
#        return true;
#    }
#
#
#    private void init(int n, Map<Integer, Set<Integer>> map, int[][] preqs) {
#        for (int i = 0; i < n; i++) {
#            map.put(i, new HashSet<>());
#        }
#        for (int[] p: preqs) {
#            //v -> u
#            int u = p[0];
#            int v = p[1];
#            map.get(v).add(u);
#        }
#    }
# }
# ‌

# topological sort
# directed graph
# check directed graph cycle
# time complexity: O(V+E): v is vertices, e is edges

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = collections.defaultdict(set)
        ins = [0 for i in range(numCourses)]
        q = collections.deque()
        self.init(numCourses, prerequisites, map, ins)

        for i in range(numCourses):
            if ins[i] == 0:
                q.append(i)

        lst = []
        while q:
            curr = q.popleft()
            lst.append(curr)
            for nxt in map[curr]:
                ins[nxt] -= 1
                if ins[nxt] == 0:
                    q.append(nxt)

        if len(lst) < numCourses:
            return []
        else:
            res = lst[:]
        return res

    def init(self, n, A, map, ins):

        for a in A:
            u = a[0]
            v = a[1]
            # prerequesit as key, the other as value
            map[v].add(u)
            ins[u] += 1


#Lee solution
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        nexts = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            _to, _from = edge[0], edge[1]
            indegree[_to] += 1
            nexts[_from].append(_to)

        queue = collections.deque([])

        # indegree = 0
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        res = []

        while queue:
            cur_course = queue.popleft()
            res.append(cur_course)
            for next_course in nexts[cur_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return res if len(res) == numCourses else []