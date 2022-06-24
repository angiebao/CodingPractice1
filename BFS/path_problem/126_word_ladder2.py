# 找到所有最短路径 bfs+dfs

# public class Q_0126_Word_Ladder_II {
#
#
#    public static void main(String[] args) {
#        Q_0126_Word_Ladder_II solution = new Q_0126_Word_Ladder_II();
#        String beginWord1 = "hit";
#        String endWord1 = "cog";
#        List<String> wordList1 = Arrays.asList("hot","dot","dog","lot","log","cog");
#
#
#        String beginWord2 = "hit";
#        String endWord2 = "cog";
#        List<String> wordList2 = Arrays.asList("hot","dot","dog","lot","log");
#
#
#        String beginWord3 = "lost";
#        String endWord3 = "miss";
#        List<String> wordList3 = Arrays.asList("most","mist","miss","lost","fist","fish");
#
#
#        Util.printListOfListString(solution.findLadders(beginWord1, endWord1, wordList1));
#        Util.printSeparator();
#        Util.printListOfListString(solution.findLadders(beginWord2, endWord2, wordList2));
#        Util.printSeparator();
#        Util.printListOfListString(solution.findLadders(beginWord3, endWord3, wordList3));
#        Util.printSeparator();
#    }
#
#
   # public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
   #     List<List<String>> res = new ArrayList<>();
   #     Set<String> set = new HashSet<>(wordList);
   #     Map<String, Set<String>> map = new HashMap<>();
   #     Map<String, Integer> dist = new HashMap<>();
   #     for (String word : set) {
   #         map.put(word, new HashSet<>());
   #     }
   #     map.put(beginWord, new HashSet<>());
   #     dist.put(beginWord, 0);
   #
   #
   #     bfs(beginWord, endWord, set, map, dist);
   #     dfs(beginWord, endWord, map, dist, new ArrayList<>(), res);
   #     return res;
   # }
   #
   #
   # // use bfs to build the graph
   # // different from other problems which init the graph at the beginning
   # private void bfs(String beginWord,
   #                  String endWord,
   #                  Set<String> set,
   #                  Map<String, Set<String>> map,
   #                  Map<String, Integer> dist) {
   #     Queue<String> q = new LinkedList<>();
   #     q.offer(beginWord);
   #
   #
   #     while (!q.isEmpty()) {
   #         boolean found = false;
   #         int size = q.size();
   #         for (int i = 0; i < size; i++) {
   #             String curr = q.poll();
   #             if (endWord.equals(curr)) {
   #                 found = true;
   #             }
   #             for (String next : getNextWords(curr, set)) {
   #                 map.get(curr).add(next);
   #                 if (!dist.containsKey(next)) {
   #                     q.offer(next);
   #                     dist.put(next, dist.get(curr) + 1);
   #                 }
   #             }
   #         }
   #         if (found) {
   #             break;
   #         }
   #     }
   # }
   #
   #
   # private void dfs(String word,
   #                  String endWord,
   #                  Map<String, Set<String>> map,
   #                  Map<String, Integer> dist,
   #                  List<String> list,
   #                  List<List<String>> res) {
   #     list.add(word);
   #     if (word.equals(endWord)) {
   #         res.add(new ArrayList<>(list));
   #     } else {
   #         System.out.println("==>" + word);
   #         for (String next : map.get(word)) {
   #             if (dist.get(next) == dist.get(word) + 1) {
   #                 dfs(next, endWord, map, dist, list, res);
   #             }
   #         }
   #     }
   #     list.remove(list.size()-1);
   # }
   #
   #
   # private Set<String> getNextWords(String word, Set<String> set) {
   #     Set<String> res = new HashSet<>();
   #     for (int i = 0; i < word.length(); i++) {
   #         for (char c = 'a'; c <= 'z'; c++) {
   #             if (c == word.charAt(i)) continue;
   #             String next = getNextWord(word, i, c);
   #             if (set.contains(next)) {
   #                 res.add(next);
   #             }
   #         }
   #     }
   #     return res;
   # }
   #
   #
   # private String getNextWord(String word, int i, char c) {
   #     char[] chars = word.toCharArray();
   #     chars[i] = c;
   #     return new String(chars);
   # }
# }
#
#
