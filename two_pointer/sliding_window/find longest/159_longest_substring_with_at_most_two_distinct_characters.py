# "pkwwke" -> 4

# “kwwk”
# “abcbbcd” -> return 4



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
# return res


# Characters
# public class Q_0159_Longest_Substring_with_At_Most_Two_Distinct_Characters {
#
#
#    public static void main(String[] args) {
#        Q_0159_Longest_Substring_with_At_Most_Two_Distinct_Characters solution = new Q_0159_Longest_Substring_with_At_Most_Two_Distinct_Characters();
#        String s1 = "eceba";
#        String s2 = "ccaabbb";
#        System.out.println(solution.lengthOfLongestSubstringTwoDistinct(s1));
#        System.out.println(solution.lengthOfLongestSubstringTwoDistinct(s2));
#    }
#
#
#    public int lengthOfLongestSubstringTwoDistinct(String s) {
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
#        int cnt = 0;
#        for (int i = 0; i < 256; i++) {
#            if (map[i] > 0) {
#                cnt++;
#            }
#            if (cnt > 2) {
#                return false;
#            }
#        }
#        return true;
#    }
# }
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        end = 0
        res = 0
        smap = [0 for i in range(256)]
        while start < len(s):
            while end < len(s):
                #substr = s[start:end]
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
        cnt = 0
        for i in range(256):
            if smap[i] > 0:
                cnt += 1
            if cnt > 2:
                return False

        return True

