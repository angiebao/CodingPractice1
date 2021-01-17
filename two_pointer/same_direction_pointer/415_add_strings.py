# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            va1 = int(num1[i]) if i >= 0 else 0
            va2 = int(num2[j]) if j >= 0 else 0

            sums = va1 + va2 + carry
            carry = sums // 10
            res.append(str(sums % 10))
            i -= 1
            j -= 1
        return "".join(res[::-1])