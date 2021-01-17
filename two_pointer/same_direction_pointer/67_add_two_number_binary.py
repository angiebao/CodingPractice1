


#--------------------------------------------

# input  "10011"
#           "10"
#
# output : "10101"
#

#创建 char array 额外的空间, 尽量不要用
#int va1 = b1.charAr(p1) - '0'
# '1' - '0' = 1
# '9' - '2' = 7
# 'c' - 'a' = 2
# stringBuilder()
# res = res + s #string

#ord('c') - ord('a') = 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        # from last to first
        res = []
        while p1 >= 0 or p2 >= 0 or carry > 0:
            val1 = ord(a[p1]) - ord('0') if p1 >= 0 else 0
            val2 = ord(b[p2]) - ord('0') if p2 >= 0 else 0

            sums = (val1) + (val2) + carry
            carry = sums // 2

            res.append(str(sums % 2))
            print(res)

            p1 -= 1
            p2 -= 1

        return "".join(res[::-1])

    def addBinary2(self, a: str, b: str) -> str:
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        # from last to first
        res = []
        while p1 >= 0 or p2 >= 0 or carry > 0:
            val1 = int(a[p1])  if p1 >= 0 else 0
            val2 = int(b[p2])  if p2 >= 0 else 0

            sums = (val1) + (val2) + carry
            carry = sums // 2

            res.append(str(sums % 2))
            print(res)

            p1 -= 1
            p2 -= 1

        return "".join(res[::-1])