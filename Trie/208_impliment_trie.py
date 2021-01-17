# 208. Implement Trie (Prefix Tree)
# public class Q_0208_Implement_Trie_Prefix_Tree {
#
#
#    public static void main(String[] args) {
#        Trie trie = new Trie();
#        trie.insert("apple");
#        System.out.println(trie.search("apple"));   // returns true
#        System.out.println(trie.search("app"));     // returns false
#        System.out.println(trie.startsWith("app")); // returns true
#        trie.insert("app");
#        System.out.println(trie.search("app"));     // returns true
#    }
#
#
#    private static class Trie {
#
#
#        private TrieNode root;
#
#
#        /** Initialize your data structure here. */
#        public Trie() {
#            root = new TrieNode();
#        }
#
#
#        public void insert(String word) {
#            TrieNode curr = root;
#            for (char c : word.toCharArray()) {
#                if (curr.next[c-'a'] == null) {
#                    curr.next[c-'a'] = new TrieNode();
#                }
#                curr = curr.next[c-'a'];
#            }
#            curr.exist = true;
#        }
#
#        /** Returns if the word is in the trie. */
#        public boolean search(String word) {
#            TrieNode curr = root;
#            for (char c : word.toCharArray()) {
#                if (curr.next[c-'a'] == null) {
#                    return false;
#                }
#                curr = curr.next[c-'a'];
#            }
#            return curr.exist;
#        }
#
#
#        /** Returns if there is any word in the trie that starts with the given prefix. */
#        public boolean startsWith(String prefix) {
#            TrieNode curr = root;
#            for (char c : prefix.toCharArray()) {
#                if (curr.next[c-'a'] == null) {
#                    return false;
#                }
#                curr = curr.next[c-'a'];
#            }
#            return true;
#        }
#
#
#        private static class TrieNode {
#            boolean exist;
#            TrieNode[] next;
#            TrieNode() {
#                exist = false;
#                next = new TrieNode[26];
#            }
#        }
#
#
#    }
#
#
# }


class TrieNode(object):
    def __init__(self, exist=False, next=None):
        self.exist = False
        self.next = [None for i in range(26)]  # initialize as None, [TrieNode() for i in range(26)]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if curr.next[ord(c) - ord('a')] is None:
                curr.next[ord(c) - ord('a')] = TrieNode()
            curr = curr.next[ord(c) - ord('a')]
        curr.exist = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if curr.next[ord(c) - ord('a')] is None:
                return False
            curr = curr.next[ord(c) - ord('a')]
        return curr.exist

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if curr.next[ord(c) - ord('a')] is None:
                return False
            curr = curr.next[ord(c) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)