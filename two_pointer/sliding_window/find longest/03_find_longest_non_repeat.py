# ==> 求最长
# while (start < 长度) {
#    while (end < 长度) {
#        移动end指针并更新
#        if (满足题目条件) {
#            更新结果
#        } else {
#            break;
#        }
#    }
#    移动start指针并更新
# }

#
# public class Q_0003_Longest_Substring_Without_Repeating_Characters {
#
#
#    public static void main(String[] args) {
#        Q_0003_Longest_Substring_Without_Repeating_Characters solution = new Q_0003_Longest_Substring_Without_Repeating_Characters();
#        String s1 = "abcabcbb";
#        String s2 = "bbbbb";
#        String s3 = "pwwkew";
#        System.out.println(solution.lengthOfLongestSubstring(s1));
#        System.out.println(solution.lengthOfLongestSubstring(s2));
#        System.out.println(solution.lengthOfLongestSubstring(s3));
#    }
#
#    public int lengthOfLongestSubstring(String s) {
#        int start = 0;
#        int end = 0;
#        int res = 0;
#        int[] map = new int[256];
#        while (start < s.length()) {
#            while (end < s.length()) {
#                map[s.charAt(end)]++;
#                end++;
#                if (isvalid(map)) {
#                    res = Math.max(res, end-start);
#                } else {
#                    break;
#                }
#            }
#            map[s.charAt(start)]--;
#            start++;
#        }
#        return res;
#    }
#
#
#    private boolean isvalid(int[] map) {
#        for (int i = 0; i < 256; i++) {
#            if (map[i] > 1) {
#                return false;
#            }
#        }
#        return true;
#    }
# }

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap = [0 for i in range(256)]
        start = 0
        end = 0
        res = 0
        while start < len(s):
            while end < len(s):

                smap[ord(s[end])] += 1
                end += 1
                if self.isValid(smap):
                    res = max(res, end - start)
                else:
                    break

            smap[ord(s[start])] -= 1
            start += 1

        return res

    def isValid(self, smap):

        for i in range(len(smap)):
            if smap[i] > 1:
                return False

        return True