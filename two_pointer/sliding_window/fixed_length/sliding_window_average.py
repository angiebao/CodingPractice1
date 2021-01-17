# 	public List<Double> findAverage(int[] nums, int k) {
# 		List<Double> res = new ArrayList<>();
# 		double sum = 0;
# 		for (int i = 0; i < k; ++i) {
# 			sum += nums[i];
# 		}
# 		res.add(sum / k);
# 		for (int r = k; r < nums.length; ++r) {
# 			sum = sum + nums[r] - nums[r - k];
# 			res.add(sum / k);
# 		}
# 		return res;
# 	}

def findAverage(nums, k):
    res = []
    sums = 0
    for i in range(k):
        sums += nums[i]
    res.append(sums/k)
    for r in range(k, len(nums)):
        sums = sums + nums[r] - nums[r-k]
        res.append(sums/k)
    return res


nums = [2,5,6,3,4,5,6]
k = 3
print(findAverage(nums, k))


def slidingWindowAverage(nums, k):
    res = []
    start = 0
    end = 0
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]
        if i >= k-1:
            res.append(sums/k)
            sums -= nums[i - k + 1]

    return res

nums = [2,5,6,3,4,5,6]
k = 3

print(slidingWindowAverage(nums, k))