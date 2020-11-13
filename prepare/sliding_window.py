# 一道sliding window sum 一道sliding window max

[1,2,5,3,7,67,4,7,3,7,34]

windowSize = 5

# sliding windows max: 递减的stack

# sliding windows sum: prefix sum


# 给两个facebook profile，设计这个profile class，并写出一个function return the connections (friends) between profile A and profile B. 例子：
#
# A : {C,F, E}
# C:  {B,D, E}


import collections

# class Node():
#     def __init__(self):


def findconnection(start, end, list1):
    graph = collections.defaultdict(list)
    for u, v in list1:
        graph[u].append(v)
        graph[v].append(u)

    traj = []
    visited = {}

    def dfs(item):
        if item not in visited:
            visited[item] = True
            for neighbor in graph[item]:

                if neighbor == end:
                    res= True
                    traj.append(neighbor)
                    return res

                if dfs(neighbor):
                    traj.append(neighbor)
                    return True
        return False



    result = dfs(start)
    traj.append(start)
    return traj[::-1]

# def findconnection(start, end, list1):
#     graph = collections.defaultdict(list)
#     for u, v in list1:
#         graph[u].append(v)
#         graph[v].append(u)
#
#     traj = []
#     visited = {}
#     result = False
#     def dfs(item):
#         nonlocal result
#         if item not in visited:
#             visited[item] = True
#             for neighbor in graph[item]:
#
#                 if neighbor == end:
#                     result = True
#
#
#             dfs(neighbor)
#
#     dfs(start)
#     return result


list1 = [[1,2],[2,5],[5,4],[5,6],[4,3], [4,10]]
print(findconnection(1, 3 ,list1))


#
# function (A, B) should return C


