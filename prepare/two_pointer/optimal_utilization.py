# Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id
# and the second integer represents a value. Your task is to find an element from a and an element form b such that
# the sum of their values is less or equal to target and as close to target as possible.
# Return a list of ids of selected elements. If no pair is possible, return an empty list.

import math
arr1 = [1,3,5,6,7, 8, 9, 10]
arr2 = [2, 4 , 6, 8, 10]
target  = 0
# binary search  method for getting the nearest smaller value

l = 0
h = len(arr1) - 1

result = False
while l <= h:
    mid = math.floor((l + h) / 2)
    if arr1[mid] < target:
        l = mid + 1
    elif arr1[mid] > target:
        h = mid - 1
    else:
        x = mid
        result = True
        break

# if the target is not find return the nearest small one
if result == False:
    if arr1[l] < target:
        x = l
    else:
        x = max(l - 1, 0)


print(arr1[x])


