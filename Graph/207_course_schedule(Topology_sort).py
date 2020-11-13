# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.

import collections
class Node:
    def __init__(self):
        # self.val = val
        self.inDegree = 0
        self.outNodes = []
        # self.start = None
        # self.end = None


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nr = len(prerequisites)
        graph = collections.defaultdict(Node)
        for relation in prerequisites:
            nextCourse, preCourse = relation[0], relation[1]
            graph[preCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegree += 1

        removedEdges = 0
        startCourses = collections.deque()
        for key, node in graph.items():
            if node.inDegree == 0:
                startCourses.append(key)

        while startCourses:
            course = startCourses.pop()

            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegree -= 1
                removedEdges += 1

                if graph[nextCourse].inDegree == 0:
                    startCourses.append(nextCourse)

        if removedEdges == nr:
            return True
        else:
            return False


numCourses = 2
prerequisites = [[1,0],[0,1]]
#Output: false
s=Solution()
s.canFinish(numCourses,prerequisites)