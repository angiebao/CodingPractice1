# 784. Letter Case Permutation

# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
#
# Return a list of all possible strings we could create. You can return the output in any order.
#
#

# Example 1:
#
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:
#
# Input: S = "3z4"
# Output: ["3z4","3Z4"]
# Example 3:
#
# Input: S = "12345"
# Output: ["12345"]
# Example 4:
#
# Input: S = "0"
# Output: ["0"]


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.helper(list(S), 0, res)
        return res

    def helper(self, chars, index, res):
        if index == len(chars):
            res.append("".join(chars))
            return
        if chars[index].isnumeric():
            self.helper(chars, index + 1, res)

        else:
            chars[index] = chars[index].lower()
            self.helper(chars, index + 1, res)
            chars[index] = chars[index].upper()
            self.helper(chars, index + 1, res)