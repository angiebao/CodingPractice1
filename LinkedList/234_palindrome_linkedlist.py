# cycles
#singly linkedlist / doubly linked list
# null or empty
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        res = []
        while fast and fast.next :
            res.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        return slow, res

    def isPalindrome(self, head):
        mid, res = self.findMiddle
        for i in range(len(res)-1, -1, -1):
            top = res[i]
            fast = mid.next
            if fast.val != top.val:
                return False

        return True

# 另一种解法，可以去reverse后面一半的linkedlist
