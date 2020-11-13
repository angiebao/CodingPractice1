# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode: # time O(N), space O(N)?
        hash = dict()
        item = head
        prev = head
        while item:
            if item.val in hash:
                #delete item
                if item == head:
                    head = item.next
                    item = head.next
                elif item.next == None:
                    prev.next = None
                    return head
                else:
                    prev.next = item.next
                    item = item.next
            else:
                hash[item.val] = 1
                prev = item
                item = item.next

        return head








head = ListNode(1)
head.next = ListNode(1)
head1 = head.next
head1.next = ListNode(2)
head2 = head1.next
head2.next = ListNode(3)
head3 = head2.next
head3.next = ListNode(3)
s= Solution()
newhead = s.deleteDuplicates(head)

while newhead:
    print(newhead.val)
    newhead = newhead.next