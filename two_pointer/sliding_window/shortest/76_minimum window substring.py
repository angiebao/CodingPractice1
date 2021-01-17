# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"

# public class Q_0076_Minimum_Window_Substring {
#
#
#    public static void main(String[] args) {
#        Q_0076_Minimum_Window_Substring solution = new Q_0076_Minimum_Window_Substring();
#        String s = "ADOBECODEBANC";
#        String t = "ABC";
#        System.out.println(solution.minWindow(s, t));
#    }
#
#
#    public String minWindow(String s, String t) {
#        if (s.length() < t.length()) {
#            return "";
#        }
#        int[] smap = new int[256];
#        int[] tmap = new int[256];
#        for (char c : t.toCharArray()) {
#            tmap[c]++;
#        }
#
#
#        int start = 0;
#        int end = 0;
#        int minlen = Integer.MAX_VALUE;
#        int minstart = 0;
#
#
#        while (end < s.length()) {
#            smap[s.charAt(end)]++;
#            end++;
#            while (start < end) {
#                if (isvalid(smap, tmap)) {
#                    int len = end-start;
#                    if (len < minlen) {
#                        minlen = len;
#                        minstart = start;
#                    }
#                    smap[s.charAt(start)]--;
#                    start++;
#                } else {
#                    break;
#                }
#            }
#        }
#
#
#        return minlen == Integer.MAX_VALUE ? "" : s.substring(minstart, minstart + minlen);
#    }
#
#
#    private boolean isvalid(int[] smap, int[] tmap) {
#        for (int i = 0; i < 256; i++) {
#            if (smap[i] < tmap[i]) {
#                return false;
#            }
#        }
#        return true;
#    }
# }

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = [0 for i in range(256)]
        smap = [0 for i in range(256)]
        minlen = float('inf')
        minstart = 0
        start = 0
        end = 0
        for i in range(len(t)):
            tmap[ord(t[i])] += 1

        while end < len(s):
            smap[ord(s[end])] += 1
            end += 1
            while start < end:
                if self.isValid(smap, tmap):
                    length = end - start
                    if length < minlen:
                        minlen = length
                        minstart = start
                    smap[ord(s[start])] -= 1
                    start += 1
                else:
                    break

        return s[minstart:minstart + minlen] if minlen != float('inf') else ""

    def isValid(self, smap, tmap):
        for i in range(256):
            if smap[i] < tmap[i]:
                return False
        return True



