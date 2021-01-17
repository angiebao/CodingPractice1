#   public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#        Deque<Integer> stack1 = new ArrayDeque<>();
#        Deque<Integer> stack2 = new ArrayDeque<>();
#        while (l1 != null) {
#            stack1.offerFirst(l1.val);
#            l1 = l1.next;
#        }
#        while (l2 != null) {
#            stack2.offerFirst(l2.val);
#            l2 = l2.next;
#        }
#        ListNode curr = null, prev = null;
#        int carry = 0;
#        while (!stack1.isEmpty() || !stack2.isEmpty() || carry != 0) {
#            int val1 = stack1.isEmpty() ? 0 : stack1.pollFirst();
#            int val2 = stack2.isEmpty() ? 0 : stack2.pollFirst();
#            int sum = val1 + val2 + carry;
#            carry = sum / 10;
#            curr = new ListNode(sum%10);
#            curr.next = prev;
#            prev = curr;
#        }
#        return curr;
#    }


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # need to return cur in the end  prev is a var to save the next location
        cur = None
        prev = None
        carry = 0

        while list1 or list2 or carry:
            val1 = list1.pop() if list1 else 0
            val2 = list2.pop() if list2 else 0

            sums = val1 + val2 + carry
            carry = sums // 10

            cur = ListNode(sums % 10)  # move cur to previous node
            cur.next = prev  # point cur.next to the saved prev (next) node
            prev = cur  # finally move prev forward

        # cur have reached head
        return cur