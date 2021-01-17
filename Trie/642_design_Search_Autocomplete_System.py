#
# public class Q_0642_Design_Search_Autocomplete_System {
#
#
#    public static void main(String[] args) {
#        String[] sentences = {"i love you", "island","ironman", "i love leetcode"};
#        int[] times = {5,3,2,2};
#        AutocompleteSystem1 autocompleteSystem1 = new AutocompleteSystem1(sentences, times);
#        System.out.println(autocompleteSystem1.input('i'));
#        System.out.println(autocompleteSystem1.input(' '));
#        System.out.println(autocompleteSystem1.input('a'));
#        System.out.println(autocompleteSystem1.input('#'));
#
#
#        Util.printSeparator();
#
#
#        AutocompleteSystem2 autocompleteSystem2 = new AutocompleteSystem2(sentences, times);
#        System.out.println(autocompleteSystem2.input('i'));
#        System.out.println(autocompleteSystem2.input(' '));
#        System.out.println(autocompleteSystem2.input('a'));
#        System.out.println(autocompleteSystem2.input('#'));
#    }
#
#
#    /*
#        Solution 1:
#        // 1. build a trie whose node saves all sentences with such prefix
#        // 2. run Top K algorithms (min heap) against the sentence frequencies
#        // write friendly, read run time is O(n) where n is the length of the input sentence
#        // *not* read friendly, since each read (autocomplete suggestions) will take O(nlogn) where n is the number of sentences with the prefix
#        // also *not* space friendly, lots of space will be consumed due to each node will save all sentences with such prefix, particularly bad for long sentences
#     */
#    (i love you, 5)
#    (island, 3)
#    (ironman, 2)
#    (i love Leetcode, 2)

#    time complexity:
#    read : n: key value pair, k, topK, O(nlog(K)) + O(len(input sentence )):
#    write: O(len)
#    space complexity:
#
#    static class AutocompleteSystem1 {
#
#
#        private static final int K = 3;
#
#
#        TrieNode root;
#        StringBuilder sb;
#
#
#        public AutocompleteSystem1(String[] sentences, int[] times) {
#            root = new TrieNode();
#            sb = new StringBuilder();
#            for (int i = 0; i < sentences.length; i++) {
#                add(sentences[i], times[i]);
#            }
#        }
#
#
#        public List<String> input(char c) {
#            List<String> res = new ArrayList<>();
#            if (c == '#') {
#                add(sb.toString(), 1);
#                sb = new StringBuilder();
#                return res;
#            }
#            sb.append(c);
#            return getTopK(sb.toString());
#        }
#
#
#        private void add(String sentence, int time) {
#            TrieNode curr = root;
#            for (char c : sentence.toCharArray()) {
#                TrieNode next = curr.children.get(c);
#                if (next == null) {
#                    next = new TrieNode();
#                    curr.children.put(c, next);
#                }
#                curr = next;
#                curr.cnt.put(sentence, curr.cnt.getOrDefault(sentence, 0) + time);
#            }
#        }
#
#
#        private List<String> getTopK(String s) {
#            TrieNode curr = root;
#            for (char c : s.toCharArray()) {
#                TrieNode next = curr.children.get(c);
#                if (next == null) {
#                    return new ArrayList<>();
#                }
#                curr = next;
#            }
#            Comparator<Map.Entry<String, Integer>> comparator = (a, b) -> a.getValue().equals(b.getValue()) ? b.getKey().compareTo(a.getKey()) : a.getValue() - b.getValue();
#            Queue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(comparator); // it must be a min heap
#            for (Map.Entry<String, Integer> entry : curr.cnt.entrySet()) {
#                pq.offer(entry);
#                if (pq.size() > K) {
#                    pq.poll();
#                }
#            }
#            List<String> res = new ArrayList<>();
#            while (!pq.isEmpty()) {
#                res.add(pq.poll().getKey());
#            }
#            Collections.reverse(res);
#            return res;
#        }
#
#
#        private static class TrieNode {
#            Map<String, Integer> cnt;
#            Map<Character, TrieNode> children;
#            TrieNode() {
#                cnt = new HashMap<>();
#                children = new HashMap<>();
#            }
#        }
#    }
#
#
#    /*
#        Solution 2:
#        1. Only leaf node saves the sentence and time
#        2. Non-leaf node saves "the" hot list of the leaf nodes
#        - This saves a lot of spaces compare with the 1st solution
#        - Read friendly (very efficient for retrieving hot suggestions), only takes O(m) where m is the length of the input
#        - Write as efficient compared with read, since each write will need to update (sort) the reference for all nodes along the trie path
#     */
#    static class AutocompleteSystem2 {
#        private static final int K = 3;
#
#
#        TrieNode root;
#        StringBuilder sb;
#
#
#        public AutocompleteSystem2(String[] sentences, int[] times) {
#            root = new TrieNode();
#            sb = new StringBuilder();
#            for (int i = 0; i < sentences.length; i++) {
#                add(sentences[i], times[i]);
#            }
#        }
#
#
#        public List<String> input(char c) {
#            List<String> res = new ArrayList<>();
#            if (c == '#') {
#                add(sb.toString(), 1);
#                sb = new StringBuilder();
#                return res;
#            }
#            sb.append(c);
#            return getTopK(sb.toString());
#        }
#
#
#        private void add(String sentence, int time) {
#            TrieNode curr = root;
#            List<TrieNode> visited = new ArrayList<>();
#            for (char c : sentence.toCharArray()) {
#                TrieNode next = curr.children.get(c);
#                if (next == null) {
#                    next = new TrieNode();
#                    curr.children.put(c, next);
#                }
#                curr = next;
#                visited.add(curr);
#            }
#            curr.s = sentence;
#            curr.t += time;
#
#
#            // curr is a reference to the leaf TrieNode
#            // only leaf node saves the sentence and time
#            // and non-leaf node saves "the" hot list of the leaf nodes
#            for (TrieNode node : visited) {
#                node.update(curr);
#            }
#        }
#
#
#        private List<String> getTopK(String s) {
#            TrieNode curr = root;
#            List<String> res = new ArrayList<>();
#            for (char c : s.toCharArray()) {
#                TrieNode next = curr.children.get(c);
#                if (next == null) {
#                    return res;
#                }
#                curr = next;
#            }
#            res.addAll(curr.hot.stream().map(e -> e.s).collect(Collectors.toList()));
#            return res;
#        }
#
#
#        private static class TrieNode implements Comparable<TrieNode> {
#            Map<Character, TrieNode> children;
#            String s; // sentence
#            int t;    // time
#            List<TrieNode> hot;
#            TrieNode() {
#                children = new HashMap<>();
#                s = null;
#                t = 0;
#                hot = new ArrayList<>();
#            }
#
#
#            @Override
#            public int compareTo(TrieNode that) {
#                return this.t != that.t ? that.t - this.t : this.s.compareTo(that.s);
#            }
#
#
#            public void update(TrieNode node) {
#                if (!hot.contains(node)) {
#                    hot.add(node);
#                }
#                Collections.sort(hot);
#                if (hot.size() > K) {
#                    hot.remove(hot.size()-1);
#                }
#            }
#        }
#    }
# }


class TrieNode(object):
    def __init__(self, s=None, t=0):
        self.K = 3
        self.s = None
        self.t = 0
        self.hot = []
        self.children = collections.defaultdict(TrieNode)

    def __gt__(self, other):
        if self.t != other.t:
            return self.t > other.t
        else:
            i = 0
            while self.s[i] == other.s[i]:
                i += 1
            return ord(self.s[i]) > ord(other.s[i])
        return

    def update(self, node):
        if node not in self.hot:
            self.hot.append(node)
        self.hot.sort(reverse=True)
        if len(self.hot) > self.K:
            self.hot.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.K = 3
        self.root = TrieNode()
        self.sb = ""
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])

    def input(self, c: str) -> List[str]:

        res = []
        if c == '#':
            self.add(self.sb, 1)
            self.sb = ""
            return res
        self.sb += c
        return self.getTopK(self.sb)

    def add(self, sentence, time):
        curr = self.root  # trie node
        visited = []  # list of trie node
        for c in sentence:
            nxt = curr.children[c]
            if not nxt:
                nxt = TrieNode()
                curr.children[c] = nxt
            curr = nxt
            visited.append(curr)
        curr.s = sentence
        curr.t += time
        #       // curr is a reference to the leaf TrieNode
        #       // only leaf node saves the sentence and time
        #       // and non-leaf node saves "the" hot list of the leaf nodes
        for node in visited:
            node.update(curr)

    def getTopK(self, s):
        curr = self.root  # trie node
        res = []
        for c in s:
            nxt = curr.children[c]
            if not nxt:
                return res
            curr = nxt
        res = [x.s for x in curr.hot]
        return res

# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you","island","iroman","i love leetcode"]
times = [5,3,2,1]

obj = AutocompleteSystem(sentences, times)
param_1 = obj.input("i")
param_2 = obj.input(" ")
param_3 = obj.input("a")
param_3 = obj.input("#")

[,],["i"],[" "],["a"],["#"]