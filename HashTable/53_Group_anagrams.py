import collections
class Solution:
    # time O（Nk logK)  N length of str, K length of longest member,
    # sorting each string is O(KlogK)
    # total info stored in d: space(NK),
    def groupAnagrams1(self, strs):
        d = dict()
        group = []
        for word in strs:
            res = ''.join(sorted(word))
            if res in d:
                d[res].append(word)
            else:
                d[res] = [word]

        return d.values()

    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))