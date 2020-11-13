
# (1) 两个表示正整数的int array相加
# (2) 找到int array中唯一一个只出现奇数次的元素

arr1 = [1,1,2,2,2,2,3,3,3,4,4]


result = 0
for i in range(len(arr1)):
    result = result ^arr1[i]

print(result)

# 给两个list return 只出现在其中一个list的element, 然后有给很多follow up (ex : 给三个list.....之类的, 应该是根据第一个给出的答案做深入)
# critical routers

#