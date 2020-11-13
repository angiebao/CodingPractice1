# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

import collections
class Gnode:
    def __init__(self):
        self.val = None
        self.inDegree = 0
        self.outNodes = []


class Solution:
    # time O(N) space O(N)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        nr = len(prerequisites)
        if nr == 0:
            return [i for i in range(numCourses)]
        self.graph = collections.defaultdict(Gnode)
        for relation in prerequisites:
            nextCourse, preCourse = relation[0], relation[1]
            self.graph[preCourse].outNodes.append(nextCourse)
            self.graph[preCourse].val = preCourse
            self.graph[nextCourse].inDegree += 1
            self.graph[nextCourse].val = nextCourse

        startCourses = []
        for key, node in self.graph.items():
            if node.inDegree == 0:
                startCourses.append(key)

        for i in range(numCourses):
            if i not in self.graph:
                startCourses.append(i)

        self.res = []
        self.status = [0] * numCourses
        self.flag = True
        for node in startCourses:
            self.dfs(node)

        if self.flag == False or len(self.res) < numCourses:
            return []

        reverse = []
        for i in range(len(self.res) - 1, -1, -1):
            reverse.append(self.res[i])

        return reverse

    def dfs(self, index):
        if self.flag == False:
            return
        node = self.graph[index]
        for n in node.outNodes:
            if self.status[n] == 0:
                self.status[n] = 1
                self.dfs(n)
            if self.status[n] == 1:
                self.flag = False
        self.res.append(index)
        self.status[index] = 2