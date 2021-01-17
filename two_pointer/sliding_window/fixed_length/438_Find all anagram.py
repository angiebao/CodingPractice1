# chr/ord

#a = [1, 2, 3, 3, 4, 2, 4]
#b=collections.Counter(a)

# 用一倍的空间 可以直接在一个arry上操作，一个在count上++， 另一个在count上--

# anagram 的题 可以用 count array， 0-25 idx-> 'a'-'z'
# check 一个string 有没有可能形成palindrome, 每个字符的count 得是偶数（偶数的时候）， 奇数的时候，只能由一个character的count是1


def findAnagrams(self, s: str, p: str) -> List[int]:
    smap = [0 for i in range(256)]
    pmap = [0 for i in range(256)]
    res = []
    for c in p:
        pmap[ord(c)] += 1

    k = len(p)
    for i in range(len(s)):
        smap[ord(s[i])] += 1
        if i >= k - 1:
            if (smap == pmap):
                res.append(i - k + 1)

            smap[ord(s[i - k + 1])] -= 1

    return res


