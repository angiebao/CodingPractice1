class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        p = [1] * n
        p[0], p[1] = 0, 0
        # only need up to  sqrt(n)
        # 2 × 6 = 12
        # 3 × 4 = 12
        # 4 × 3 = 12
        # 6 × 2 = 12
        for i in range(2, int(math.sqrt(n)) + 1):
            if p[i]:
                j = i + i
                while j < n:
                    p[j] = 0  # mark as not prime
                    j += i
        count = 0
        for i in range(n):
            if p[i]:
                count += 1
        return count

    # def isPrime(self, n):
    #     for i in range(2, floor(sqrt(n)) + 1):
    #         for j in range(i, floor(n/2) + 1):
    #             if i*j == n:
    #                 return False
    #     return True