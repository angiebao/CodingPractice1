from queue import PriorityQueue as pq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        q = pq()
        # sort the item
        intervals.sort(key=lambda x: x[0])
        # use a variable to store the max
        minRoom = 1
        if len(intervals) == 0:
            return 0

        q.put((intervals[0][1], intervals[0][0]))

        for item in intervals[1:]:
            # meeting does not overlap, next element start time larger than the previous meeting end time, then pop the top element, push the current elemenet,

            if item[0] >= q.queue[0][0]:
                # sort by the end time
                q.get()

            q.put((item[1], item[0]))

            if len(q.queue) > minRoom:
                minRoom = len(q.queue)

        return minRoom
