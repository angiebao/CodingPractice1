class Solution():
    # in place heapImpl sort
    # TIME O(nlog(n)) 不稳定
    def heap_sort(self, arr):
        self.length = len(arr)
        for i in range(len(arr)//2 -1, -1, -1): # time O(N log N)
            self.heapify(arr, i)
        for i in range(len(arr)): # time O(N log N)
            arr[0], arr[self.length - 1] = arr[self.length - 1] , arr[0]
            self.length -= 1
            self.heapify(arr, 0)
        return arr
    def heapify(self, arr, i): # put largest on top  , time O(logN)
        left  = 2*i +1
        right = 2*i +2
        largest = i
        if left < self.length  and arr[left] > arr[largest]:
            largest = left
        if right <self.length  and arr[right] > arr[largest]:
            largest = right

        if (largest != i):
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest)

arr= [20, 10, 8, 7, 11, 5, 9]
s= Solution()
arr_sorted=s.heap_sort(arr)

print(arr_sorted)