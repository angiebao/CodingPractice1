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