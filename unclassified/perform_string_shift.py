import collections


class Solution:
    def stringShift(self, s: str, shift) -> str:

        n = len(s)
        shiftCount = collections.defaultdict(int)
        for i in range(len(shift)):
            if shift[i][0] == 0:
                shiftCount[0] += shift[i][1]
            else:
                shiftCount[1] += shift[i][1]

        movement = shiftCount[1] - shiftCount[0]
        if movement > 0:
            moveright = abs(movement) % n
            s = s[-moveright:] + s[:-moveright]
        else:
            moveleft = abs(movement) % n
            s = s[moveleft:] + s[:moveleft]

        return s