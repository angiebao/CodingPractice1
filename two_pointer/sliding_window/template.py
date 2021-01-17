# ==> 求最短
# while (end < 长度) {
#    移动end指针并更新
#    while (start < end) {
#        if (满足题目条件) {
#            1. 更新结果
#            2. 移动start指针并更新temp结果
#        } else {
#            break;
#        }
#    }
# }
# fix length
#
# for (i in range(长度)) {
#        更新temp 结果
#        if (i >= k - 1) {
#            更新结果
#            更新 temp结果
#        }
#    }
#    返回结果
# }

# ==> 求最长
# while (start < 长度) {
#    while (end < 长度) {
#        移动end指针并更新temp结果
#        if (满足题目条件) {
#            更新结果
#        } else {
#            break;
#        }
#    }
#    移动start指针并更新temp结果
# }

