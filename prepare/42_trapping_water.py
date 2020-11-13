# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height: List[int]) -> int:
        # find the leftmax and right max then calcualte the traping water  using left max - height[left] or righmax - height[right]
        # use two pointer to achive goal in one loop

        left = 0
        right = len(height) - 1
        leftmax = float('-inf')
        rightmax = float('-inf')
        ans = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
                left += 1
            else:  # height[left] >= height[right]
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]

                right -= 1

        return ans