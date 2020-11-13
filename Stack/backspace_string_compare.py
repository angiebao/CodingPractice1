class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1 = []
        res2 = []
        for i in range(len(S)):
            if S[i] != '#':
                res1.append(S[i])
        else:
            if i != 0:
                res1.pop()

        for i in range(len(T)):
            if T[i] != '#':
                res2.append(T[i])
        else:
            if i != 0:
                res2.pop()


        if res1 == res2:
            return True

        return False


