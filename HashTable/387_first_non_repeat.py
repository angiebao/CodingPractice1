

class Solution:
    # story the values in harsh table first
    # and loop through the characters to find if in the dictionary the value is
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1
