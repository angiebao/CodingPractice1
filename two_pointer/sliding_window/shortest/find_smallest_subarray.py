# Example
# Int array [4,3,7,5]  find the smallest length of a subarray which has sum >= K
#
# array : [4,3,7,5]
# K : 10
#
# # all positive values.
#
# [1,1] 2
#
Def findSmallestSubarray(numbers, K):
	Start = 0
	End = 0
	Minlength = float(‘inf’)
	Sums = 0
	While end<len(numbers):
		Sum += numbers[end]
        End += 1

		While start < end:

			If sums>=k:
				Minlength = min(minlength, end - start)
				Sums -= numbers[start]
                Start += 1

			Else:
				Break

   	Return minlength if minlength != float(‘inf’) else -1