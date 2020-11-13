class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # use a depth frist search for recursive method to explore all the possible expression

        opened = 1
        cur = '('
        self.result = []
        depth = 1
        self.dfs(cur, opened, depth, n)
        return self.result

    def dfs(self, cur, depth, opened, n):
        if depth == 2 * n:
            if opened == 0:
                self.result.append(cur)
            return

        if opened > 0:
            self.dfs(cur + ')', depth + 1, opened - 1, n)

        self.dfs(cur + '(', depth + 1, opened + 1, n)