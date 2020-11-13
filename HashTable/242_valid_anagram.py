class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()

        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True

        for i in range(len(s)):
            item1 = s[i]
            item2 = t[i]
            if item1 not in d1:
                d1[item1] = 1
            else:
                d1[item1] += 1

            if item2 not in d2:
                d2[item2] = 1
            else:
                d2[item2] += 1

        for k, v in d1.items():
            if k not in d2:
                return False
            else:
                if v != d2[k]:
                    return False

        return True
