#  Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2


# public class Q_0253_Meeting_Rooms_II {
#
#
#    public static void main(String[] args) {
#        Q_0253_Meeting_Rooms_II solution = new Q_0253_Meeting_Rooms_II();
#        int[][] intervals1 = {{0, 30},{5, 10},{15, 20}};
#        int[][] intervals2 = {{7,10},{2,4}};
#        System.out.println(solution.minMeetingRooms1(intervals1));
#        System.out.println(solution.minMeetingRooms1(intervals2));
#        Util.printSeparator();
#        System.out.println(solution.minMeetingRooms2(intervals1));
#        System.out.println(solution.minMeetingRooms2(intervals2));
#    }
#
#
#    /*
#    Solution 1: 扫描线解法 ： swipe line
#     */
#    public int minMeetingRooms1(int[][] intervals) {
#        if (intervals == null || intervals.length == 0 || intervals[0].length == 0) {
#            return 0;
#        }
#
#
#        Queue<Tuple> pq = new PriorityQueue<>();
#        for (int[] interval : intervals) {
#            int start = interval[0];
#            int end = interval[1];
#            pq.offer(new Tuple(start, true));
#            pq.offer(new Tuple(end, false));
#        }
#
#
#        int res = 0;
#        int cnt = 0;
#        while (!pq.isEmpty()) {
#            Tuple curr = pq.poll();
#            if (curr.isstart) {
#                cnt++;
#            } else {
#                cnt--;
#            }
#            res = Math.max(res, cnt);
#        }
#
#
#        return res;
#    }
#
#
#    private static class Tuple implements Comparable<Tuple> {
#        private int time;
#        private boolean isstart;
#        Tuple (int time, boolean isstart) {
#            this.time = time;
#            this.isstart = isstart;
#        }
#
#
#        @Override
#        public int compareTo(Tuple that) {
#            if (this.time != that.time) {
#                return this.time - that.time;
#            } else {
#                if (this.isstart && that.isstart) return 0;
#                else return this.isstart ? 1 : -1;
#            }
#        }
#    }
#


#     /*
#      Solution 2: TreeMap解法
#      */
#    public int minMeetingRooms2(int[][] intervals) {
#        Map<Integer, Integer> map = new TreeMap<>();
#        for (int[] interval : intervals) {
#            map.put(interval[0], map.getOrDefault(interval[0], 0) + 1);
#            map.put(interval[1], map.getOrDefault(interval[1], 0) - 1);
#        }
#
#
#        int res = 0;
#        int cnt = 0;
#        for (int val : map.values()) {
#            cnt += val;
#            res = Math.max(res, cnt);
#        }
#        return res;
#    }
#
#
# }

# #  heap  # time complexity O(nlog(n))
# #   treemap # BST 添加一个元素 log(n) 平衡的， insert N次，所以是nlog(n)

#       insert    top/first (pop)    remove
# BST    logn     O(1)                logn
# heap   logn     O(1)                O(n)

# with comparator

class Tuple(object):
    def __init__(self, val: int, isstart: bool):
        self.val = val
        self.isstart = isstart

    def __gt__(self, other):
        if self.val != other.val:
            return self.val > other.val
        else:
            if self.isstart:
                return True
            else:
                return False
        return


from queue import PriorityQueue


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = PriorityQueue()
        for interval in intervals:
            pq.put(Tuple(interval[0], True))
            pq.put(Tuple(interval[1], False))

        res = 0
        cnt = 0
        while not pq.empty():
            t = pq.get()
            if t.isstart:
                cnt += 1
            else:
                cnt -= 1

            res = max(res, cnt)
        return res



#s扫描线 解法
from queue import PriorityQueue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pq = PriorityQueue()
        for interval in intervals:
            pq.put((interval[0], True))
            pq.put((interval[1], False))

        res = 0
        cnt = 0
        while not pq.empty():
            cur, isStart = pq.get()
            if isStart:
                cnt += 1
            else:
                cnt -= 1

            res = max(res, cnt)
        return res

# 解法2
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
