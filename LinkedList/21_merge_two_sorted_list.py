# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # time O(N+M), space O(1)
    def mergeTwoLists_iter(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val<= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2= l2.next

            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return prehead.next

    # time O(n+m) space space (n+m), first call does not return , until the the ends of l1 or l2 reached
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) ->ListNode:
        newHead = None
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            newHead = l1
            newHead.next = self.mergeTwoLists(l1.next, l2)
        elif l1.val > l2.val:
            newHead = l2
            newHead.next = self.mergeTwoLists(l1, l2.next)

        return newHead


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
s = Solution()
head = s.mergeTwoLists(l1, l2)

while head:
    print(head.val)
    head = head.next