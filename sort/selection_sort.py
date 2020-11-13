
"""
https://www.cnblogs.com/onepixel/p/7674659.html
"""


# selection sort O(N^2) 不稳定

def selection_sort(x):
    for i in range(0, len(x) - 1):
        minindex = i
        for j in range(i, len(x) - 1):  # O(n^2)
            if x[j + 1] < x[minindex]:
                minindex = j + 1
        x[i], x[minindex] = x[minindex], x[i]
    return x


x5 = [1, 5, 8, 2, 3, 9, 7]
x1 = [1]
x2 = []
x3 = [-1 - 5, -3, -8, -10, -4]
x4 = [9, 8, 7, 6, 5, 4, 3, 2]

for x in [x1, x2, x3, x4, x5]:
    x_unsort = x.copy()
    x_sort = selection_sort(x)
    print(x_unsort)
    print(x_sort)
    print("-----------")