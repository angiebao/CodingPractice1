
class Solution:
    def reverseWords(self, s: str) -> str:

        new_data = s.split()
        p1, p2 = 0, len(new_data) - 1
        while p1 < p2:
            new_data[p1], new_data[p2] = new_data[p2], new_data[p1]
            p1 += 1
            p2 -= 1
        return " ".join(new_data)

s =  Solution()
s.reverseWords()