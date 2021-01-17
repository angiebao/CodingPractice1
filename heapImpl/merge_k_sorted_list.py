#k way merge sort : 比如 朋友圈 按时间排序 display出来 ， 但是会加一些ranking的算法

# first method: use divide and conquer
# divide by each pair of list,
# then merge sort recursively each pair

# 2->3->7
#
# 1->2>3>5>6>7
# nlog(m)

# heap with merge sort
# N log(K)
# O(logk) for every pop and insertion to heap, do N times, so Nlog(k)
# k is the number of linked lists.

# N is number of node in the final list
