# 127. Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#
#         # use a intermediate state h*t, *it , hi*, store all the combination in a dictionary
#         # first store the begin word in the queue, make a dictionary to story the visited words
#         if endWord not in wordList:  # or not endWord or not beginWord or not wordList:
#             return 0
#
#         # L = len(wordList)
#         L = len(beginWord)
#         combo_dict = collections.defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 # there might be several word has the same intermedidate state
#                 combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
#
#         q = collections.deque()
#         q.append((beginWord, 1))
#         visited = {}
#         visited[beginWord] = True
#
#         while q:
#             cur, level = q.popleft()
#             for i in range(L):
#
#                 intermediate_cur = cur[:i] + '*' + cur[i + 1:]
#
#                 for word in combo_dict[intermediate_cur]:
#
#                     # if visited do nothing
#                     if word not in visited:
#                         q.append((word, level + 1))
#                         visited[word] = True
#                     if word == endWord:
#                         return level + 1
#                         # combo_dict[intermediate_cur] = []
#
#         return 0

import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)  # this means it is visited

                        queue.append([next_word, length + 1])
        return 0


# java

#
# public class Q_0127_Word_Ladder {
#    public static void main(String[] args) {
#        Q_0127_Word_Ladder solution = new Q_0127_Word_Ladder();
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
#        String beginWord3 = "hit";
#        String endWord3 = "hot";
#        List<String> wordList3 = Arrays.asList("hot","dot");
#
#
#        System.out.println(solution.ladderLength(beginWord1, endWord1, wordList1));
#        System.out.println(solution.ladderLength(beginWord2, endWord2, wordList2));
#        System.out.println(solution.ladderLength(beginWord3, endWord3, wordList3));
#    }
#
#
#    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
#        Set<String> set = new HashSet<>(wordList);
#
#
#        int len = bfs(beginWord, endWord, set);
#        return len;
#    }
#
#
#    private int bfs(String beginWord, String endWord, Set<String> set) {
#        Queue<String> q = new LinkedList<>();
#        Set<String> visited = new HashSet<>();
#        q.offer(beginWord);
#        visited.add(beginWord);
#
#
#        int len = 0;
#        while (!q.isEmpty()) {
#            len++;
#            int size = q.size();
#            for (int i = 0; i < size; i++) {
#                String curr = q.poll();
#                if (curr.equals(endWord)) {
#                    return len;
#                }
#                for (String next : getNextWords(curr, set)) {
#                    if (visited.add(next)) {
#                        q.offer(next);
#                    }
#                }
#            }
#        }
#        return 0;
#    }
#
#
#    private List<String> getNextWords(String s, Set<String> set) {
#        List<String> res = new ArrayList<>();
#        for (int i = 0; i < s.length(); i++) {
#            for (char c = 'a'; c <= 'z'; c++) {
#                if (c != s.charAt(i)) {
#                    String next = getNextWord(s, c, i);
#                    if (set.contains(next)) {
#                        res.add(next);
#                    }
#                }
#            }
#        }
#        return res;
#    }
#
#
#    private String getNextWord(String s, char c, int i) {
#        char[] chars = s.toCharArray();
#        chars[i] = c;
#        return new String(chars);
#    }
# }


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)

        length = self.bfs(beginWord, endWord, s)
        return length

    def bfs(self, beginWord, endWord, s):
        q = collections.deque()
        q.append(beginWord)
        visited = set()

        length = 0
        while q:
            length += 1
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr == endWord:
                    return length
                words = self.getNextWords(curr, s)
                for nxt in words:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        return 0

    def getNextWords(self, curr, s):
        res = []
        for i in range(len(curr)):
            for c in range(ord('a'), ord('z') + 1):
                if c != ord(curr[i]):
                    nxt = curr[0:i] + chr(c) + curr[i + 1:]
                    if nxt in s:
                        res.append(nxt)
        return res


