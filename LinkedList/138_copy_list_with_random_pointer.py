# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
# public class Q_0138_Copy_List_with_Random_Pointer {
#
#
#    public Node copyRandomList(Node head) {
#        if (head == null) {
#            return null;
#        }
#
#
#        Map<Node, Node> map = new HashMap<>();
#
#
#        // build map
#        Node curr = head;
#        while (curr != null) {
#            map.put(curr, new Node(curr.val));
#            curr = curr.next;
#        }
#
#
#        // deep copy
#        curr = head;
#        while (curr != null) {
#            map.get(curr).next = map.get(curr.next);
#            map.get(curr).random = map.get(curr.random);
#            curr = curr.next;
#        }
#        return map.get(head);
#    }
#
#
#    // Definition for a Node.
#    class Node {
#        int val;
#        Node next;
#        Node random;
#
#
#        public Node(int val) {
#            this.val = val;
#            this.next = null;
#            this.random = null;
#        }
#    }
# }
‌


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        curr = head
        maps = dict()

        # build map
        while curr:
            maps[curr] = Node(curr.val)
            curr = curr.next

        # deep copy
        curr = head
        while curr:
            maps[curr].next = maps[curr.next] if curr.next else None
            maps[curr].random = maps[curr.random] if curr.random else None
            curr = curr.next

        return maps[head]

