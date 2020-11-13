# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #time O(N/2) = O(N), space O(1)
    def middleNode(self, head):
        half = head
        current = head
        if head == None:
            return head

        while current and current.next:
            current = current.next.next

            half = half.next

        return half