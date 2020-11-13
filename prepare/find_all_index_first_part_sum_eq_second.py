# find all index i where sum(arr[0:i]) == sum(arr[i:])
# do it in space O(1)
def allIndex(arr):
    preSum = 0
    # calcualte the prefix sum
    # total sum
    totalsum = 0
    res = []
    for i in range(len(arr)):
        totalsum += arr[i]
    for i in range(len(arr)):
        preSum += arr[i]

        if preSum*2 == totalsum:
            res.append(i)

    return res


arr = [1,2,3,4,3,2,5, 5, 5]

print(allIndex(arr))
