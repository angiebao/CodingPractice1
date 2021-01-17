#    private TreeSet<Integer> minheap;
#    private TreeSet<Integer> maxheap;
#
#    public double[] medianSlidingWindow(int[] nums, int k) {
#        Comparator<Integer> comparator = (i, j) -> nums[i] != nums[j] ? Integer.compare(nums[i], nums[j]) : i - j;
#
#        // the elements in the heap are the index of the given array
#        minheap = new TreeSet<>(comparator);
#        maxheap = new TreeSet<>(comparator.reversed());
#        double[] res = new double[nums.length - k + 1];
#        for (int i = 0; i < nums.length; i++) {
#            add(i);
#            if (i >= k-1) {
#                res[i-k+1] = getMedian(nums);
#                remove(i-k+1);
#            }
#        }
#        return res;
#    }
#
#    private void add(int i) {
#        if (maxheap.size() <= minheap.size()) {
#            minheap.add(i);
#            maxheap.add(minheap.pollFirst());
#        } else {
#            maxheap.add(i);
#            minheap.add(maxheap.pollFirst());
#        }
#    }
#
#    private void remove(int i) {
#        if (maxheap.contains(i)) {
#            maxheap.remove(i);
#        } else {
#            minheap.remove(i);
#        }
#    }
#
#    private double getMedian(int[] nums) {
#        int size = minheap.size() + maxheap.size();
#        if (size % 2 == 0) {
#            return ((double)nums[minheap.first()] + (double)nums[maxheap.first()]) / 2;
#        } else {
#            return nums[maxheap.first()];
#        }
#    }