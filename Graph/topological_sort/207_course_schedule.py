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
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.


# this problem just ask if there is loop or not.

# python solution

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Solution:
            def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                indegree = [0 for _ in range(numCourses)]
                nexts = [[] for _ in range(numCourses)]
                for edge in prerequisites:
                    _to, _from = edge[0], edge[1]
                    indegree[_to] += 1
                    nexts[_from].append(_to)

                queue = collections.deque([])

                # indegree = 0
                for course in range(numCourses):
                    if indegree[course] == 0:
                        queue.append(course)
                count = 0

                while queue:
                    cur_course = queue.popleft()
                    count += 1
                    for next_course in nexts[cur_course]:
                        indegree[next_course] -= 1
                        if indegree[next_course] == 0:
                            queue.append(next_course)

                return count == numCourses

