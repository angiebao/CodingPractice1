class Solution:
    def PredictTheWinner(self, nums ): #: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        memo = dict()

        firstpalyer = self.getMax(nums, 0, n, memo)

        return True if firstpalyer >= sum(nums) / 2 else False

    def getMax(self, card, start, end, memo):

        if end - start == 1:
            return card[start]

        if tuple(card[start:end]) in memo:
            maxresult = memo[tuple(card[start:end])]
            return maxresult

        takefirst = sum(card[start:end]) - self.getMax(card, start + 1, end, memo)
        takelast = sum(card[start:end]) - self.getMax(card, start, end - 1, memo)

        maxresult = max(takefirst, takelast)

        memo[tuple(card[start:end])] = maxresult

        return maxresult

nums = [3,4,5,6]

s = Solution()
s.PredictTheWinner(nums)