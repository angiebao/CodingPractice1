# Find the largest multiple of 3 | Set 1 Given an array of non-negative integers.
# Find the largest multiple of 3 that can be formed from array elements.
# For example, if the input array is {8, 1, 9}, the output should be “9 8 1”,
# and if the input array is {8, 1, 7, 6, 0}, output should be “8 7 6 0”.
import itertools
class Solution():
    def multipleThree(self, arr):
        n = len(arr)
        max_length = float('-inf')
        for i in range(n):
            combs = set(itertools.combinations(arr, i))
            for comb in combs:
                if i > max_length and sum(comb) %3 ==0:
                    result = list(comb)
                    max_length = i
        return result


arr = [8,1,7,6,0,5,2,6,8,2,5,6,2,5,2,3,5,8,7,3,1]
s = Solution()
result = s.multipleThree(arr)
print(result)

