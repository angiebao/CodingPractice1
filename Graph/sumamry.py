
# Graph
#
# 套路
# 1. Find number of connected components: time O(V+ E) , O(n^2 + n), O(n^2) to build map, becuase of n(n-1) edges to loop through?
# 2. Cycle detection : topological sort tdo determine if there is cycle
# 3. Graph clone
#

# 4.有向/无向
# 5.有环/无环 : topology sort,
#     DAG directed acyclic graph 有向无环图 , not necessarily tree
#     tree: 1. one root, 2.  each node has one parent(except root), 3. no cycle
#           in practice: 1. number of nodes == number of edges + 1;
# #                      2. all nodes connected
#     use BFS: node indegree ==0 to put in queue

# 6.静态图 static connectivity: number of island not change
# 7.动态图 incremental connectivity : union find : number of island 2, hard, O(k + m*n) vs brute force  bfs O(k*m*n) () each time of incremental, do a BFS
#    first build the ocnstructor, O(m * n), [1,2,3,4,5,6,7,8,9]
#
# function find is O(1) time complexity, amortized
#
# 8.DFS from boundary or given source



#
# types:
#  adjacency list: [1: [ 5, 2], 2 : [1], 3: [4], 4: [3]]
#  adjacency matrix: [[x,x,x,]
#                     [x,x,x]
#                     [x,x,x]
#                     ]
# edge list [1,2], [2,5], [3, 4], [1,5] ]
#
#

# template
# 1. init (for example friend circle )
# 2. dfs




#
# 练习题
#
# 一般是先build graph // pattern
#
# Graph Valid Tree
# Accounts Merge
# Number of Connected Components in an Undirected Graph
# Friend Circles
# Flood Fill
# Number of Enclaves
#
# 课后练习
# Number of Islands
# Max Area of Island
# Number of Distinct Islands
# Accounts Merge
# Sentence Similarity II
# Similar String Groups
# Surrounded Regions
# Keys and Rooms
# Number of Closed Islands
