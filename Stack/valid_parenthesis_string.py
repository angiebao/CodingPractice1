class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) ==0:
            return True
        d1 = set()
        d1.add(0)
        for i in range(len(s)):
            d2 = set()
            if s[i] == '(':
                for item in d1:
                    item = item + 1
                    d2.add(item)
            if s[i] == ')':
                for item in d1:
                    item = item - 1
                    if item >= 0:
                        d2.add(item)
            if s[i] == '*':
                for item in d1:
                    item1 = item - 1
                    item2 = item
                    item3 = item + 1
                    if item1 >=0:
                        d2.add(item1)
                    d2.add(item2)
                    d2.add(item3)
            d1 = d2.copy()


        for item in d2:
            if item == 0:
                return True

        return False



    def checkValidString1 (self, s: str) -> bool:
        lo = 0
        hi = 0;
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if (hi < 0):
                break
            lo = max(lo, 0);

        return lo == 0;


expression = "()())*)"
expression = "(())*)"
expression= ")("
s= Solution()
print(s.checkValidString(expression))