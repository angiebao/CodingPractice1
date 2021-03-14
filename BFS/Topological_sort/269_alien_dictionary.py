# ublic class Q_0269_Alien_Dictionary {
#
#
#    public static void main(String[] args) {
#        Q_0269_Alien_Dictionary solution = new Q_0269_Alien_Dictionary();
#        String[] words1 = {"wrt", "wrf", "er", "ett", "rftt"};
#        String[] words2 = {"z", "x"};
#        String[] words3 = { "z", "x", "z"};
#        System.out.println(solution.alienOrder1(words1));
#        System.out.println(solution.alienOrder1(words2));
#        System.out.println(solution.alienOrder1(words3));
#        Util.printSeparator();
#        System.out.println(solution.alienOrder2(words1));
#        System.out.println(solution.alienOrder2(words2));
#        System.out.println(solution.alienOrder2(words3));
#    }
#
#
#    /*
#        Solution 1: BFS
#     */
#    public String alienOrder1(String[] words) {
#        Map<Character, Set<Character>> map = new HashMap<>();
#        Map<Character, Integer> ins = new HashMap<>();
#        if (!init1(words, map, ins)) return "";
#        return bfs(map, ins);
#    }
#
#
#    private String bfs(Map<Character, Set<Character>> map, Map<Character, Integer> ins) {
#        Queue<Character> q = new LinkedList<>();
#        for (Map.Entry<Character, Integer> entry : ins.entrySet()) {
#            if (entry.getValue() == 0) {
#                q.offer(entry.getKey());
#            }
#        }
#
#
#        StringBuilder sb = new StringBuilder();
#        while (!q.isEmpty()) {
#            char curr = q.poll();
#            sb.append(curr);
#            for (char next : map.get(curr)) {
#                int in = ins.get(next);
#                if (--in == 0) {
#                    q.offer(next);
#                }
#                ins.put(next, in);
#            }
#        }
#
#
#        return sb.length() == map.size() ? sb.toString() : "";
#    }
#
#
#    private boolean init1(String[] words, Map<Character, Set<Character>> map, Map<Character, Integer> ins) {
#        for (String word : words) {
#            for (char c : word.toCharArray()) {
#                map.putIfAbsent(c, new HashSet<>());
#                ins.putIfAbsent(c, 0);
#            }
#        }
#        for (int i = 0; i < words.length; i++) {
#            for (int j = i+1; j < words.length; j++) {
#                boolean hasDiff = false;
#                for (int k = 0; k < Math.min(words[i].length(), words[j].length()); k++) {
#                    char c1 = words[i].charAt(k);
#                    char c2 = words[j].charAt(k);
#                    if (c1 == c2) continue;
#
#
#                    hasDiff = true;
#                    Set<Character> set = map.get(c1);
#                    if (set.add(c2)) {
#                        ins.put(c2, ins.get(c2) + 1);
#                    }
#
#
#                    break;
#                }
#                if (!hasDiff && words[i].length() > words[j].length()) return false;
#            }
#        }
#        return true;
#    }
#
#
#    /*
#        Solution 2: DFS
#     */
#    public String alienOrder2(String[] words) {
#        Map<Character, Set<Character>> map = new HashMap<>();
#        int[] visited = new int[128];
#        if (!init2(words, map)) return "";
#
#
#        char curr = words[0].charAt(0);
#        Stack<Character> stack = new Stack<>();
#        for (String word : words) {
#            for (char c : word.toCharArray()) {
#                if (visited[curr] == 0 && !dfs(map, visited, curr, stack)) {
#                    return "";
#                }
#            }
#        }
#        StringBuilder sb = new StringBuilder();
#        while (!stack.isEmpty()) {
#            sb.append(stack.pop());
#        }
#        return sb.toString();
#    }
#
#
#    private boolean dfs(Map<Character, Set<Character>> map, int[] visited, char curr, Stack<Character> stack) {
#        visited[curr] = 1;
#        for (char next : map.get(curr)) {
#            if (visited[next] == 2) continue;
#            if (visited[next] == 1) return false;
#            if (!dfs(map, visited, next, stack)) return false;
#        }
#        visited[curr] = 2;
#        stack.push(curr);
#        return true;
#    }
#
#
#    private boolean init2(String[] words, Map<Character, Set<Character>> map) {
#        for (String word : words) {
#            for (char c : word.toCharArray()) {
#                map.putIfAbsent(c, new HashSet<>());
#            }
#        }
#        for (int i = 0; i < words.length; i++) {
#            for (int j = i+1; j < words.length; j++) {
#                boolean hasDiff = false;
#                for (int k = 0; k < Math.min(words[i].length(), words[j].length()); k++) {
#                    char c1 = words[i].charAt(k);
#                    char c2 = words[j].charAt(k);
#                    if (c1 == c2) continue;
#
#
#                    hasDiff = true;
#                    map.get(c1).add(c2);
#                    break;
#                }
#                if (!hasDiff && words[i].length() > words[j].length()) return false;
#            }
#        }
#        return true;
#    }
# }

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        map = collections.defaultdict(set)
        ins = collections.defaultdict(int)
        hasDiff = self.init(words, map, ins)
        if not hasDiff:
            return ""
        else:
            return self.bfs(map, ins)

    def bfs(self, map, ins):
        q = collections.deque()
        for entry, entryvalue in ins.items():
            if entryvalue == 0:
                q.append(entry)

        sb = ""
        while q:
            curr = q.popleft()
            sb += curr
            for nxt in map[curr]:
                ins[nxt] -= 1
                if ins[nxt] == 0:
                    q.append(nxt)

        if len(sb) != len(map):
            return ""
        return sb

    def init(self, words, map, ins):
        for word in words:
            for c in word:
                if c not in map:
                    ins[c] = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                hasDiff = False
                for k in range(min(len(words[i]), len(words[j]))):
                    c1 = words[i][k]
                    c2 = words[j][k]
                    if c1 == c2:
                        continue
                    hasDiff = True

                    if c2 not in map[c1]:
                        map[c1].add(c2)
                        ins[c2] += 1

                    break

                if (not hasDiff) and (len(words[i]) > len(words[j])):
                    return False

        return True