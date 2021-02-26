#quick sort
# time complexity O(nlog n), space complexity O(nlogn )
# 最好 O（n） 最差 O（n^2）
def quicksort(l):
    if len(l) < 1:
        return l

    pivot = l[0]
    l1 = [i for i in l if i < pivot]
    l2 = [i for i in l if i > pivot]
    l1 = quicksort(l1)
    l2 = quicksort(l2)

    l = l1 + [pivot] + l2
    return l


#l = [1,2,5,1, 4,3,0]
l=[0,0,2,2,1,1]
print(quicksort(l))

class Solution:
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        mid = self.partition(A, start, end)
        self.quick_sort(A, start, mid - 1)
        self.quick_sort(A, mid + 1, end)


    def partition(self, A, start, end):
        m, pivot = start, A[start]
        for i in range(start + 1, end + 1):
            if A[i] < pivot:
                m += 1
                self.swap(A, m, i)
        self.swap(A, start, m)
        return m


    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp


S=Solution()
S.quick_sort(l, 0 , len(l) - 1 )
print(l)

# function quickSort(arr, left, right) {
#     varlen = arr.length,
#         partitionIndex,
#         left = typeofleft != 'number'? 0 : left,
#         right = typeofright != 'number'? len - 1 : right;
#
#     if(left < right) {
#         partitionIndex = partition(arr, left, right);
#         quickSort(arr, left, partitionIndex-1);
#         quickSort(arr, partitionIndex+1, right);
#     }
#     returnarr;
# }
#
# function partition(arr, left ,right) {     // 分区操作
#     varpivot = left,                      // 设定基准值（pivot）
#         index = pivot + 1;
#     for(vari = index; i <= right; i++) {
#         if(arr[i] < arr[pivot]) {
#             swap(arr, i, index);
#             index++;
#         }
#     }
#     swap(arr, pivot, index - 1);
#     returnindex-1;
# }
#
# function swap(arr, i, j) {
#     vartemp = arr[i];
#     arr[i] = arr[j];
#     arr[j] = temp;

##-------------------------------------------------------------------
# seond way to write partition

# public class Solution {
#     /**
#      * @param A: an integer array
#      * @return: nothing
#      */
#     public int[] sortArray(int[] nums) {
#         // write your code here
#         quickSort(nums, 0, nums.length - 1);
#         return nums;
#     }
#
#     private void quickSort(int[] nums, int start, int end) {
#         if (start >= end) {
#             return;
#         }
#         int mid = partition(nums, start, end);
#         quickSort(nums, start, mid - 1);
#         quickSort(nums, mid + 1, end);
#     }
#
#     private int partition(int[] nums, int start, int end) {
#         int pivot = nums[start];
#         int i = start + 1;
#         int j = end;
#         while (i <= j) {
#             while (i <= j && nums[i] <= pivot) {
#                 i++;
#             }
#             while (i <= j && nums[j] > pivot) {
#                 j--;
#             }
#             if (i > j) {
#                 break;
#             }
#             int temp = nums[i];
#             nums[i] = A[j];
#             nums[j] = temp;
#             j--;
#             i++;
#         }
#         nums[start] = nums[j];
#         nums[j] = pivot;
#         return j;
#     }
# }