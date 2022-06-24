# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# public class Q_0017_Letter_Combinations_of_a_Phone_Number {
#
#
#    private static final String[] phone = {"","","abc","edf","ghi","jkl","mno","pqrs","tuv","wxyz"};
#
#
#    public static void main(String[] args) {
#        Q_0017_Letter_Combinations_of_a_Phone_Number solution = new Q_0017_Letter_Combinations_of_a_Phone_Number();
#        String digits = "23";
#        System.out.println(solution.letterCombinations(digits));
#    }
#
#
#    public List<String> letterCombinations(String digits) {
#        List<String> res = new ArrayList<>();
#        if (digits.length() == 0) {
#            return res;
#        }
#        helper(digits, 0, "", res);
#        return res;
#    }
#
#
#    private void helper(String digits, int index, String curr, List<String> res) {
#        if (index == digits.length()) {
#            res.add(curr);
#            return;
#        }
#        String letters = phone[digits.charAt(index) - '0'];
#        for (int i = 0; i < letters.length(); i++) {
#            helper(digits, index+1, curr+letters.charAt(i), res);
#        }
#    }
# }

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         res = []
#         if len(digits) == 0:
#             return res
#         temp = ""
#         index = 0
#         self.phone = ["", "", "abc", "edf", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
#         self.helper(digits, index, temp, res)
#         return res
#
#     def helper(self, digits, index, curr, res):
#         # when index equals the length of digits, no need to go inside the loop and get letters= self.phone[ord(digits[index]) - ord('0')]
#         if index == len(digits):
#             res.append(curr)
#             return
#         letters = self.phone[ord(digits[index]) - ord('0')]
#         # a - >
#         #     e, -> index == len(digit)-> return and next loop get d
#         #     d,-> index == len(degit) -> return and next loop get f
#         #     f - > index == len(digit) - > return and next loop to b
#         # b ->
#         #     e-> index == len(digit)-> return and next loop get d
#         #     d,-> index == len(degit) -> return and next loop get f
#         #     f - > index == len(digit) - > return and next loop to b
#         for i in range(len(letters)):
#             self.helper(digits, index + 1, curr + letters[i], res)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.d = dict()
        self.d['2'] = 'abc'
        self.d['3'] = 'def'
        self.d['4'] = 'ghi'
        self.d['5'] = 'jkl'
        self.d['6'] = 'mno'
        self.d['7'] = 'pqrs'
        self.d['8'] = 'tuv'
        self.d['9'] = 'wxyz'

        visited = set()
        index = 0
        curr = ''  # current word combination
        res = []  # all the path

        self.dfs(digits, index, curr, res)
        return res

    def dfs(self, digits, index, curr, res):
        # curr is the current word
        if index == len(digits):
            res.append(curr)
            return

        letters = self.d[digits[index]]
        # enter next level in the graph/ finding neighbors
        for l in letters:
            self.dfs(digits, index + 1, curr + l, res)

# Time complexity : O(3^N ×4 ^M) where N is the number of digits in the input
# that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and
# M is the number of digits in the input that maps to 4 letters (e.g. 7, 9),
# and N+M is the total number digits in the input.
#
# Space complexity :  since one has to keep 3^N * 4^M solutions

