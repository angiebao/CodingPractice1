class Solution:
    def isHappy(self, n: int) -> bool:
        #         slow = n
        #         fast = self.sumSquare(n)

        #         while slow != fast:
        #             slow = self.sumSquare(slow)
        #             fast = self.sumSquare(fast)
        #             fast = self.sumSquare(fast)

        #         if slow !=1:
        #             return False
        #         if slow == 1 :
        #             return True

        # use harsh table:
        d = dict()
        result = n
        while result != 1:
            if result not in d:
                d[result] = 1
            elif result in d and result != 1:
                return False
            result = self.sumSquare(result)

        if result == 1:
            return True

    def sumSquare(self, n):
        digits = str(n)
        sums = 0
        for i in range(0, len(digits)):
            sums += (int(digits[i])) ** 2
        return sums

