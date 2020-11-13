# 503. Next Greater Element II
# Medium
# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # put a copy of nums after nums, becuase we only need to loop at most two times through nums

        nums_copy = nums + nums
        # use the stack to store the max value so far, if we met a value larger than the value at the top of the stack, we remove the top of element at the top of the stack until the current met value is smaller, if this result in an empty stack, then the result will be -1 for the current element
        stack = []
        result = [0 for i in range(len(nums_copy))]

        for i in range(len(nums_copy) - 1, -1, -1):
            cur = nums_copy[i]

            while stack and cur >= stack[-1]:
                stack.pop()

            if (not stack):
                result[i] = -1
            else:
                result[i] = stack[-1]

            stack.append(cur)

        return result[:len(nums)]