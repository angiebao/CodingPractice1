# 答案二分
# 模板
#
# int lo = 1, hi = max;             // 1. 找到可行解的范围
# while (lo + 1 < hi) {
#     int mid = lo + (hi - lo)/2;  // 2. 猜答案
#     if (check(mid)) {              // 3. 检验答案
#         lo = mid;                     // 4. 调整搜索范围
#     } else {
#         hi = mid;                     // 4. 调整搜索范围
#     }
# }
# return lo or hi?                   // 5. 返回最终结果
#
# sqrt(x) solution lies in (0, x) 之间
# 1. 0, 1,2,3,4,5 try one by one
# 2. logx complexity, find mid of (0, x)



# leetcode 69 find sqrt(x)
#
# 1. double or int
# a. integer
# 2. x range, positiive? negative? (0.x), (1,x)
#
# example x = 16, lo = 3, hi = 4, final if else need to
# def mySqrtInt(x):
#     lo = 0
#     hi = x
#     while (lo + 1 < hi):
#         mid =  low + (hi - low)/2
#         if mid < x/mid
#             lo = mid
#     else