# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    # time O(2N)=O(N) Space O(2N)=O(N)
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()

        for i in range(len(s)):
            item1 = s[i]
            item2 = t[i]
            if item1 not in d1:
                d1[item1] = item2
            else:
                if d1[item1] != item2:
                    return False

        for k, v in d1.items():
            if v not in d2:
                d2[v] = 1
            else:
                return False
        return True

s= Solution()

print(s.isIsomorphic("ab", "aa"))