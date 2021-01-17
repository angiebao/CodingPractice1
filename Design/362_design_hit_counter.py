# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?



# public class Q_0362_Design_Hit_Counter {
#
#
#    public static void main(String[] args) {
#        // Radix sort + bucket implement - more predictable on space usage
#        HitCounter1 counter1 = new HitCounter1();
#        counter1.hit(1);
#        counter1.hit(2);
#        counter1.hit(3);
#        System.out.println(counter1.getHits(4));
#        counter1.hit(300);
#        System.out.println(counter1.getHits(300));
#        System.out.println(counter1.getHits(301));
#
#
#        Util.printSeparator();
#
#
#        // Queue only implementation - easy to implement but not space friendly
#        // consider the situation when there is a lot of hits in a very short period of time
#        HitCounter2 counter2 = new HitCounter2();
#        counter2.hit(1);
#        counter2.hit(2);
#        counter2.hit(3);
#        System.out.println(counter2.getHits(4));
#        counter2.hit(300);
#        System.out.println(counter2.getHits(300));
#        System.out.println(counter2.getHits(301));
#    }
#
#
#    static class HitCounter1 {
#
#
#        private static final int SECONDS = 300;
#        int[] hits;
#        int[] times;
#
#
#        /** Initialize your data structure here. */
#        public HitCounter1() {
#            hits = new int[SECONDS];
#            times = new int[SECONDS];
#        }
#
#
#        /** Record a hit.
#         @param timestamp - The current timestamp (in seconds granularity). */
#        public void hit(int timestamp) {
#            int idx = timestamp % SECONDS;
#            if (timestamp != times[idx]) {
#                times[idx] = timestamp;
#                hits[idx] = 0;
#            }
#            hits[idx]++;
#        }
#
#
#        /** Return the number of hits in the past 5 minutes.
#         @param timestamp - The current timestamp (in seconds granularity). */
#        public int getHits(int timestamp) {
#            int cnt = 0;
#            for (int i = 0; i < SECONDS; i++) {
#                if (timestamp - times[i] < SECONDS) {
#                    cnt += hits[i];
#                }
#            }
#            return cnt;
#        }
#    }
#
#
#    static class HitCounter2 {
#
#
#        private static final int SECONDS = 300;
#        private Queue<Integer> q;
#
#
#        /** Initialize your data structure here. */
#        public HitCounter2() {
#            q = new LinkedList<>();
#        }
#
#
#        /** Record a hit.
#         @param timestamp - The current timestamp (in seconds granularity). */
#        public void hit(int timestamp) {
#            q.offer(timestamp);
#        }
#
#
#        /** Return the number of hits in the past 5 minutes.
#         @param timestamp - The current timestamp (in seconds granularity). */
#        public int getHits(int timestamp) {
#            while (!q.isEmpty() && timestamp - q.peek() >= SECONDS) {
#                q.poll();
#            }
#            return q.size();
#        }
#    }
# }

# space efficient

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SECONDS = 300
        self.hits = [0 for i in range(self.SECONDS)]
        self.times = [0 for i in range(self.SECONDS)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        if timestamp != self.times[idx]:
            self.times[idx] = timestamp
            self.hits[idx] = 0
        # this is for one tiemstamp to hit multiple times
        self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        cnt = 0
        for i in range(self.SECONDS):
            if timestamp - self.times[i] < self.SECONDS:
                cnt += self.hits[i]

        return cnt
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# not space efficient
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SECONDS = 300
        self.q = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.q and timestamp - self.q[0] >= self.SECONDS:
            self.q.popleft()
        return len(self.q)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)