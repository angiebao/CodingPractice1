def dfs(s, words, i, mem):
    if s[i:] in mem:
        return mem[s[i:]]

    if i == len(s):
        return []

    cur_result = []
    for j in range(i + 1, len(s) + 1):
        word = s[i:j]
        if word in words:
            rest = dfs(s, words, j, mem)
            if rest:
                for item in rest:
                    cur_result.append(word + ' ' + item)
            if j == len(s):
                cur_result.append(word)
    mem[s[i:]] = cur_result
    return cur_result


class Solution:
    def wordBreak(self, s: str, wordDict) :
        mem = {}
        return dfs(s, wordDict, 0, mem)

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

solution = Solution()

print(solution.wordBreak(s, wordDict))