# 1202. Smallest String With Swaps
# Medium
# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
#
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
#
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
#
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.


import collections
class Solution:
    # find which are the nodes in the same group, then they can exchange however they want, they we just need to group, and sort within the group.

    def smallestStringWithSwaps(self, s: str, pairs): # List[List[int]]) -> str:
        # union find using find function and merge function
        # Time O(VlogV + E), space O(V+V)
        self.parents = [i for i in range(len(s))]
        self.pairs = pairs

        if len(pairs) == 0:
            return s

        for (index1, index2) in pairs:  # O(E)
            # if not self.is_connected(index1, index2):
            self.merge(index1, index2)

        # groups = {self.find(x) for x in self.parents}
        subsets = collections.defaultdict(list)

        for i in range(len(s)):  # O(V)
            subsets[self.find(i)].append(s[i])

        for k, v in subsets.items():  # Worst O(VlogV)
            subsets[k].sort()
            subsets[k] = subsets[k][::-1]

        result = []
        for i in range(len(s)):  # O(V)
            if subsets[self.find(i)]:
                item = subsets[self.find(i)].pop()
                result.append(item)

        return "".join(result)

    def find(self, index):
        if self.parents[index] != index:
            root = self.find(self.parents[index])
            self.parents[index] = root
            return root
        return index

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.parents[root_a] = root_b

s = "dcab"
pairs = [[0,3],[1,2]]

s= Solution()
s.smallestStringWithSwaps(s, pairs)