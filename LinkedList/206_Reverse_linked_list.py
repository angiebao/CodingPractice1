# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList0(self, head: ListNode) -> ListNode:
        item =head
        reversedHead = None

        if head:  # make sure the list is not empty, space: O(N), time: O(N)
            NodeArray = []
            while item:
                # print(item.val)
                # item = item.next
                #iteratively reverse the linked list
                NodeArray.append(item)
                item = item.next

            reversedHead = NodeArray[len(NodeArray)-1]
            reversedTail = NodeArray[len(NodeArray) - 1]
            for i in range(len(NodeArray)-2, -1, -1):
                reversedTail.next = NodeArray[i]
                reversedTail = reversedTail.next
                print(reversedTail.val)
            reversedTail.next = None

        return reversedHead

    def reverseList_iter(self, head: ListNode) -> ListNode:  #space O(1), Time O(N)
        prev = None
        curr = head
        while curr: #when Current == none, we reach the last element
            nextNode = curr.next  # save the curr.next
            curr.next = prev      # point curr.next to prev
            prev = curr           #  move next, let prev be the current
            curr = nextNode       # move next, let the current be the next
        return prev

#    public ListNode reverseList(ListNode head) {
    #        if (head == null || head.next == null) {
    #            return head;
    #        }
    #        ListNode dummy = new ListNode(0);
    #        dummy.next = head;
    #        ListNode prev = head;
    #        ListNode curr = prev.next;
    #        while (curr != null) {
    #            prev.next = curr.next;
    #            curr.next = dummy.next;
    #            dummy.next = curr;
    #            curr = prev.next;
    #        }
    #        return dummy.next;
    #    }

    def reverseList(self, head:ListNode) -> ListNode:     # space (N), because would go n level deep, time: O(N)
        if head == None or head.next == None: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


    def reverseList_recurCount(self, head:ListNode, count = 0) -> ListNode:
        if head == None or head.next == None: return head
        p = self.reverseList_recurCount(head.next, count +1)
        head.next.next = head
        if count == 0:
            head.next = None
        return p

head = ListNode(1)
head.next = ListNode(2)
head1= head.next
head1.next= ListNode(3)
head2 = head1.next
head2.next = ListNode(4)
head3=head2.next
head3.next = ListNode(5)
#ListNode(5) has automatically assigned the next to be none


s=Solution()
rList = s.reverseList_recurCount(head)

while rList:
    print(rList.val)
    rList = rList.next