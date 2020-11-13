class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two sums I: O(n) time, space(O(n))
        # two sums II: O(n) time, space O(1)
        # 从两边逼近
        low = 0
        high = len(numbers) - 1

        while low < high:

            if numbers[low] + numbers[high] > target:
                if numbers[low] > numbers[high]:
                    low += 1
                else:
                    high -= 1
            elif numbers[low] + numbers[high] < target:
                if numbers[low] < numbers[high]:
                    low += 1
                else:
                    high -= 1
            else:
                return [low + 1, high + 1]