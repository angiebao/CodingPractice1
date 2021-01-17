# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words,
# one of the first string's permutations is the substring of the second string.
#
# Example 1:
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0 for i in range(256)]
        l2 = [0 for i in range(256)]

        for i in range(len(s1)):
            l2[ord(s1[i])] += 1

        k = len(s1)
        for i in range(len(s2)):
            l1[ord(s2[i])] += 1
            if i >= k - 1:
                if (l1 == l2):
                    return True

                l1[ord(s2[i - k + 1])] -= 1

        return False