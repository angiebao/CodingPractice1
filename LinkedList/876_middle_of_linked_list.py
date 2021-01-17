# class Solution {
#     public ListNode middleNode(ListNode head) {
#         ListNode slow = head;
#         ListNode fast = head;
#         while (fast != null && fast.next != null) {
#             slow = slow.next;
#             fast = fast.next.next;
#         }
#         return slow;
#     }
# }

# 2>3>3>2
# return first 3


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