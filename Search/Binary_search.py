import math
def BinarySearch(x, T, p, r):
    low = p
    high =  r
    while low <= high:
        mid = math.floor((low + high)/2)
        if x < T[mid]:
            high = mid-1
        elif x > T[mid]:
            low = mid + 1
        else:
            return mid
    return -1

T = [3,4,5,6,7,8,9,10, 11, 12, 13]
x = 4

p = 0
r = len(T) -1

print(BinarySearch(x, T, p, r))
