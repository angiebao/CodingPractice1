# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0,0, [], res)

        return res

    def helper(self, n , left, right, path, res):
        if len(path) == n*2:
            res.append("".join(path))

        if left < n:
            path.append("(")
            self.helper(n, left + 1, right, path, res)
            path.pop()

        if left> right:
            path.append(")")
            self. helper(n, left, right + 1, path, res)
            path.pop()