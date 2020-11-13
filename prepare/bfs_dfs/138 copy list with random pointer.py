


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



import collections

class Solution:
    def __init__(self):
        self.visitedHash = collections.defaultdict(Node)


    def copyRandomList(self, head: 'Node') -> 'Node':

        # deep copy of the random list
        if head == None:
            return None

        if head in self.visitedHash:
            # if we already stored the current node, just use it
            return self.visitedHash[head]

        #if this node is never seen
        # create a new node with the value same as old node
        node  = Node(head.val)

        # save this node to visited node
        self.visitedHash[head] = node

        # recursively copy the remaining linked list starting once from the next pointer and then from the random pointer
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

s= Solution()

#randomlist = [[7,None],[13,0],[11,4],[10,2],[1,0]]

head = Node(7)
head.random = None

head.next = Node(13)
head.next.random = Node(0)

head.next.next = Node(11)
head.next.next.random =  Node(4)

head.next.next.next = Node(10)
head.next.next.next.random = Node(2)

head.next.next.next.next = Node(1)
head.next.next.next.next.random = Node(0)

copied_list = s.copyRandomList(head)
print(copied_list)