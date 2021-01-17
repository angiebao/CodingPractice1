# public class Q_0295_Find_Median_from_Data_Stream {
#
#
#    public static void main(String[] args) {
#        Q_0295_Find_Median_from_Data_Stream.MedianFinder mf = new Q_0295_Find_Median_from_Data_Stream.MedianFinder();
#        mf.addNum(1);
#        mf.addNum(2);
#        System.out.println(mf.findMedian());
#        mf.addNum(3);
#        System.out.println(mf.findMedian());
#    }
#
#
#    static class MedianFinder {
#
#
#        private Queue<Integer> maxheap;
#        private Queue<Integer> minheap;
#
#
#        /** initialize your data structure here. */
#        public MedianFinder() {
#            //use minheap to store the larger half(smallest on top), use maxheap to store the smaller half(largest on top).

#            minheap = new PriorityQueue<>();
#            maxheap = new PriorityQueue<>(Collections.reverseOrder());
#        }
#
#
#        public void addNum(int num) {
#            if (maxheap.size() <= minheap.size()) {
#                minheap.offer(num);
#                maxheap.offer(minheap.poll());
#            } else {
#                maxheap.offer(num);
#                minheap.offer(maxheap.poll());
#            }
#        }
#
#
#        public double findMedian() {
#            int size = maxheap.size() + minheap.size();
#            if (size % 2 == 0) {
#                return ((double)maxheap.peek() + (double)minheap.peek()) / 2.0;
#            } else {
#                return (double)maxheap.peek();
#            }
#        }
#    }
#
#
# }

from queue import PriorityQueue


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = PriorityQueue()
        self.maxheap = PriorityQueue()

    def addNum(self, num: int) -> None:
        # add number to max heap， maxheap might have one more element than min heap
        if (self.maxheap.qsize()) <= (self.minheap.qsize()):
            # get the smaller value compared with current num and put in maxheap
            self.minheap.put(num)
            self.maxheap.put(-1 * self.minheap.get())
        # add number to minheap
        else:
            # get the larger value compared with current num and put in the minheap
            self.maxheap.put(-1 * num)
            self.minheap.put(-1 * self.maxheap.get())

    def findMedian(self) -> float:
        size = self.minheap.qsize() + self.maxheap.qsize()
        if size % 2 == 0:
            return (self.minheap.get() + (-1) * self.maxheap.get()) / 2.0
        else:
            return -1 * self.maxheap.get()

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_1 = obj.findMedian()
print(param_1)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)

# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]

