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

# public class Q_0784_Letter_Case_Permutation {
#
#
#    public static void main(String[] args) {
#        Q_0784_Letter_Case_Permutation solution = new Q_0784_Letter_Case_Permutation();
#        String S1 = "a1b1";
#        String S2 = "3z4";
#        String S3 = "12345";
#        System.out.println(solution.letterCasePermutation(S1));
#        System.out.println(solution.letterCasePermutation(S2));
#        System.out.println(solution.letterCasePermutation(S3));
#    }
#
#
#    // clarification:
#    // 1. could have both lower and upper case letters
#    // 2. consist only of letters and digits
#    public List<String> letterCasePermutation(String S) {
#        List<String> res = new ArrayList<>();
#        helper(S.toCharArray(), 0, res);
#        return res;
#    }
#
#
#    private void helper(char[] chars, int index, List<String> res) {
#        if (index == chars.length) {
#            res.add(new String(chars));
#            return;
#        }
#        if (Character.isDigit(chars[index])) {
#            helper(chars, index+1, res);
#        } else {
#            chars[index] = Character.toLowerCase(chars[index]);
#            helper(chars, index+1, res);
#            chars[index] = Character.toUpperCase(chars[index]);
#            helper(chars, index+1, res);
#        }
#    }
# }