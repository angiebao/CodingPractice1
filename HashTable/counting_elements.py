class Solution:
    def countElements(self, arr) :
        d = dict()

        for item in arr:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        count = 0
        for k, v in d.items():
            if k + 1 in d:
                count +=  d[k]

        return count


s = Solution()
print(s.countElements([1,3,2,3,5,0]))