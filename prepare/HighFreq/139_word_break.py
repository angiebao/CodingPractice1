class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming, record for current i position, if the previous ones have a match if valid[i] == 1.
        # then loop throught the wordict to find out if there is any match word, if there is , valid[i+len(w)] =1
        n = len(s)
        m = len(wordDict)
        valid = [0 for i in range(n + 1)]
        valid[0] = 1

        for i in range(n + 1):

            if valid[i]:
                for w in wordDict:
                    if s[i:i + len(w)] == w:
                        valid[i + len(w)] = 1
        return valid[n]
