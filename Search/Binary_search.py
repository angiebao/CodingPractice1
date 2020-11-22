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

def BinarySearch_robust(x, T, p, r):
    low = p
    high = r
    while low + 1 < high:
        mid = low + math.floor((high-low)/2) # 防止溢出
        if x < T[mid]:
            high = mid
        elif x > T[mid]:
            low = mid
        else:
            low =  mid # 如果元素里有多个 1 2 2 2 3， 找2, 找upper bond

    if(T[high] == x):
        return high
    elif (T[low] == x):
        return low
    else:
        return -1
# index out of bond :
# need to check arr[idx -1]
# 变种
T1 = [0, 1,2,2,2,3]
p1 = 0
r1 = len(T1) - 1
x1 = 2

T = [3,4,5,6,7,8,9,10, 11, 12, 13]
x = 4
p = 0
r = len(T) -1

#print(BinarySearch(x, T, p, r))
print(BinarySearch_robust(x1, T1, p1, r1 ))