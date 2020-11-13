class Solution:
    def wordBreak(self, s: str, wordDict):
        res = []
        self.dfs(s, wordDict, 0, [], res)
        return res

    def dfs(self, s, words, i, cur, res):
        if i == len(s):
            res.append(' '.join(cur))

        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if word in words:
                cur.append(word)
                self.dfs(s, words, j, cur, res)
                cur.pop()  # pop cat out, then in the last level, we can choose cats


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

solution = Solution()

print(solution.wordBreak(s, wordDict))
