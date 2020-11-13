class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            print(ch)
            if ch in ('{', '[', '('):
                stack.append(ch)
                continue
            if ch in ('}', ']', ')'):
                if stack:
                    last = stack.pop()
                else:
                    return False
                if ch == '}' and last == '{':
                    continue
                elif ch == ']' and last == '[':
                    continue
                elif ch == ')' and last == '(':
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False



expression ='{[()]}'

expression =']'
#expression = '()'
expression =''
s=Solution()
print(s.isValid(expression))