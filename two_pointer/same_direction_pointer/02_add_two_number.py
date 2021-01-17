# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        iterhead = ListNode(0)
        dummy = iterhead
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curSum = val1 + val2 + carry
            carry = (curSum // 10)

            iterhead.next = ListNode(curSum % 10)
            iterhead = iterhead.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# public class Q_0002_Add_Two_Numbers {
#
#
#    public static void main(String[] args) {
#        Q_0002_Add_Two_Numbers solution = new Q_0002_Add_Two_Numbers();
#        ListNode l1 = new ListNode(2);
#        l1.next = new ListNode(4);
#        l1.next.next = new ListNode(3);
#
#        ListNode l2 = new ListNode(5);
#        l2.next = new ListNode(6);
#        l2.next.next = new ListNode(4);
#
#
#        Util.printListNode(solution.addTwoNumbers(l1, l2));
#    }
#
#
#    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#        ListNode dummy = new ListNode(0);
#        ListNode curr = dummy;
#        int carry = 0;
#        while (l1 != null || l2 != null || carry != 0) {
#            int val1 = l1 == null ? 0 : l1.val;
#            int val2 = l2 == null ? 0 : l2.val;
#
#
#            int sum = val1 + val2 + carry;
#            carry = sum / 10;
#            curr.next = new ListNode(sum % 10);
#            curr = curr.next;
#
#
#            l1 = (l1 == null) ? null : l1.next;
#            l2 = (l2 == null) ? null : l2.next;
#        }
#        return dummy.next;
#    }
# }

def addTwoNumber(l1,l2):
    iterhead = ListNode(0)
    dummy  = iterhead
    while l1 or l2 or carry !=0:
        val1 = l1.val  if l1 else 0
        val2 = l2.val if l2 else 0
        sum =
