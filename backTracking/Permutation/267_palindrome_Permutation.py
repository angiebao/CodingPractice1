#
# public class Q_0267_Palindrome_Permutation_II {
#
#
#    public static void main(String[] args) {
#        Q_0267_Palindrome_Permutation_II solution = new Q_0267_Palindrome_Permutation_II();
#        String s1 = "aabb";
#        String s2 = "abc";
#        System.out.println(solution.generatePalindromes(s1));
#        System.out.println(solution.generatePalindromes(s2));
#    }
#
#
#    // clarification:
#    // 1. return empty list if no palindromic permutation can be formed
#    // 2. could be either lower or upper case
#    public List<String> generatePalindromes(String s) {
#        List<String> res = new ArrayList<>();
#        int[] map = new int[256];
#        for (char c : s.toCharArray()) {
#            map[c]++;
#        }
#
#
#        // 1. if there is more than one odd count char, no palindromic permutation can be formed
#        // 2. find the odd count char, which should be placed in the middle of the palindromic string
#        // 3. save characters to a list
#        int oddCnt = 0;
#        String mid = "";
#        List<Character> list = new ArrayList<>();
#        for (int i = 0; i < 256; i++) {
#            if (map[i] % 2 == 1) {
#                oddCnt++;
#                mid = (char)i + "";
#            }
#            for (int k = 0; k < map[i] / 2; k++) {
#                #already sorted so smart, becasuse loop through 0 to 256
#                list.add((char)i);
#            }
#        }
#        if (oddCnt > 1) {
#            return res;
#        }
#
#
#        List<String> permuted = permute(list);
#        for (String str : permuted) {
#            res.add(str + mid + new StringBuilder(str).reverse().toString());
#        }
#        return res;
#    }
#
#
#    private List<String> permute(List<Character> list) {
#        List<String> res = new ArrayList<>();
#        helper(new StringBuilder(), new boolean[list.size()], list, res);
#        return res;
#    }
#
#
#    private void helper(StringBuilder sb, boolean[] visited, List<Character> list, List<String> res) {
#        int len = sb.length();
#        if (sb.length() == list.size()) {
#            res.add(sb.toString());
#            return;
#        }
#        for (int i = 0; i < list.size(); i++) {
#            if (!visited[i]) {
#                sb.append(list.get(i));
#                visited[i] = true;
#                helper(sb, visited, list, res);
#                visited[i] = false;
#                sb.setLength(len);
#
#
#                while (i+1 < list.size() && list.get(i) == list.get(i+1)) i++;
#            }
#        }
#    }
# }


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        res = []
        maps = [0 for i in range(256)]

        for c in s:
            maps[ord(c)] += 1

        #       1. if there is more than one odd count char, no palindromic permutation can be formed
        #       2. find the odd count char, which should be placed in the middle of the palindromic string
        #       3. save half of characters to a list
        oddCnt = 0
        mid = ""
        lists = []
        for i in range(256):
            if maps[i] % 2 == 1:
                oddCnt += 1
                mid = chr(i) + ""

            for k in range(math.floor(maps[i] / 2)):
                lists.append(chr(i))

        # have more than two characters have odd count, then this cannot be a palendrom word
        if oddCnt > 1:
            return res

        # 4. permute the half of the characters and get a list of permuted  words
        permuted = self.permute(lists)

        # 5 form the palendrom word
        for strsList in permuted:
            strs = "".join(strsList)
            res.append(strs + mid + strs[::-1])

        return res

    def permute(self, lst):
        result = []
        visited = [False for i in range(len(lst))]
        self.helper([], visited, lst, result)
        return result

    def helper(self, temp, visited, lst, res):
        if len(temp) == len(lst):
            res.append(temp[:])
            return
        itr = iter(range(len(lst)))
        for i in itr:
            if not visited[i]:
                visited[i] = True
                temp.append(lst[i])
                self.helper(temp, visited, lst, res)
                # back tracking
                visited[i] = False
                temp.pop()

                while i + 1 < len(lst) and lst[i] == lst[i + 1]:
                    next(itr)
                    i += 1



