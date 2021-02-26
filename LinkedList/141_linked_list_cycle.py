class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#
# class SinglelyLinkedList:
#     def __int__(self):
#         self.tail = None
#
#     def append(self, data):
#         node = ListNode.data
#         if self.head:
#             self.head.next = node
#             self.head = node
#
#         else:
#             self.tail = node
#             self.head = node

# method 1 - hash
class Solution(object):
    def hasCycle_n2(self, head): # search fucntion, time complexity is O(n^2), because for each element, we need to search

        arraylist = []
        item = head
        while item:
            if item in arraylist:
                rtype = True
                return rtype
            else:
                arraylist.append(item)
                item = item.next

        rtype = False

        return rtype

    def hasCycle_hash(self, head):  # time complexity is O(1), Space complexity is O(n)?

        hash = dict()
        item = head
        while item:
            if item in hash:
                rtype = True
                return rtype
            else:
                hash[item] = 1
                item = item.next

        rtype = False

        return rtype

# method 2 two pointer
    # space complexity if O(2)=O(1), with a cycle, Time complexity is O(N), without a cycle, Time complexity is O(N+K) = O(N)
    # N is the non-cycle lenght, K is the cycle length,

    def hasCycle_TwoPointer(self, head):
        slow = head
        if head: # check if empty list
            fast = head.next
        else:
            return False
        if slow == fast:   # check if the list is only one element that is cycled
            return True

        while slow != fast and fast:
            if slow.next:
                slow = slow.next
            else:
                break
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    break
            else:
                break

            if slow == fast:
                return True

        return False

# shortest way
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast.next and fast:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# head = ListNode(3)
# head.next = ListNode(2)

# head1 = head.next
# head1.next = ListNode(0)

# head2 = head1.next
# head2.next = ListNode(-4)

# head2.next.next = head1

# head = ListNode(None)
head = ListNode(1)
head.next = head

s = Solution()

print(s.hasCycle(head))