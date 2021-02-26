# method 1
# 1. copy node
# hashmap: key(old)->value(new), only copy value
#
# 2. copy ref
# newHead.next - oldhead.next
# newHead.rand = hm.get(oldhead.random)
#
# method 2:
# 1->1"-2-2"->3-3"
#
# 1'.next = 1.next.next
# 1'.random = 1.random.next