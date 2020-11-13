# class Solution:
#     #Time O(2N) space O(2N)
#     def findRepeatedDnaSequences(self, s: str) :
#         d = dict()
#         arr = []
#         for i in range(0, len(s) - 9):
#             if s[i:i + 10] not in d:
#                 d[s[i:i + 10]] = 1
#             else:
#                 d[s[i:i + 10]] += 1
#
#         for k, v in d.items():
#             if v > 1:
#                 arr.append(k)
#
#         return arr


class Solution:
    #time: O(N-L), L=10, Space O(N-L) to keep the hashset
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n <= L:
            return []

        to_int = {'A': 0, 'G': 2, 'C': 1, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        bitmask = 0
        seen, output = set(), set()

        for start in range(0, n - L + 1):
            if start != 0:
                bitmask <<= 2  # shift left to free 2 bit
                bitmask |= nums[start + L - 1]  # add a new 2bit number in the last two bits
                bitmask &= ~(3 << 2 * L)
            else:
                # less than the 10 bit initially
                for i in range(0, L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                output.add(s[start:start + L])
            seen.add(bitmask)

        return output