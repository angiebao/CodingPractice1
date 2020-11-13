# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue as pq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # k pointers

        q = pq()
        i = 0
        for item in lists:
            if item:
                q.put((item.val, i, item)) # the priority queue will sort the heap
                i += 1

        dummy = ListNode(0)
        iterhead = dummy

        while not q.empty():

            _, _, node = q.get()
            iterhead.next = node
            iterhead = iterhead.next    # move to next
            if node.next:
                q.put((node.next.val, i, node.next))
                i += 1
        return dummy.next