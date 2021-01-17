# anagram, for example, eat, aet are anagram
# 把A变成B 需要几步
# 大小写 特殊字符 空格？
import collections

def minimumSteps(s, t):
        d = collections.Counter(s)
        count = 0
        for c in t:
            if c in d and d[c]>0:
                count += 1
                d[c] -= 1
        return len(s) - count
# test
#aba bab
# D = (a:2, b:1)
# count 1 d = {2:2, b:0}
# Count 2 d = {a:1, b:0}
#
# aba bac
# D = {a :2, b :1}
# count 1 d={a:2, :0}