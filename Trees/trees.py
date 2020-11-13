from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self, node = None):
        self.root_node = node

    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)


    def breadth_first_traversal(self):
        list_of_nodes = []
        traversal_queue = deque([self.root_node])

        while len(traversal_queue)>0:
            node = traversal_queue.popleft() # 双向队列, root_node
            list_of_nodes.append(node)
            #print(node.data)

            if node.left_child:
                traversal_queue.append(node.left_child)
                #print(node.left_child.data)

            if node.right_child:
                traversal_queue.append(node.right_child)
                #print(node.right_child.data)

        return list_of_nodes

    def insert(self, data):
        node  = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
        while True:
            parent = current
            if node.data < parent.data:   # we found the place to insert
                current = current.left_child  # check the left child
                if current == None: # there is no left child, then this is the place to insert the node
                    parent.left_child = node
                    return
            else:               #  node.data > parent.data, then we go to the right child, if right child is not empty, we start the next iteration and let parent= current
                current = current.right_child   # check the right child
                if current == None:  # reach the end of the tree
                    parent.right_child = node
                    return


    def get_node_with_parent(self, data):
        parent = None
        current  = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)

    def remove(self, data):
        parent, node  = self.get_node_with_parent(data)
        if parent is None and node is None:
            return False
        #get children count

        children_count = 0
        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count= 0
        else:
            children_count=1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data   # replace the node data with the left most node in the right tree

            if parent_of_leftmost_node.left_child == leftmost_node: #parent has left child
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:   # parent has no left_child
                parent_of_leftmost_node.right_child = leftmost_node.right_child


     #searching a tree
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child



# build a tree-----------------------------------------------------------------------------------------------
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4
n2.right_child = n5
n3.left_child = n6
n3.right_child = n7

T= Tree(n1)
# insert in a tree------------------------------------------------------------------------------------------
#T.insert(9)

#breadth first traversal -----------------------------------------------------------------------------------
List_of_nodes1 = T.breadth_first_traversal()
found = T.search(7)
print("find the element in Tree %s" %found)

# remove from a tree----------------------------------------------------------------------------------------
#T.remove(7)

List_of_nodes2 = T.breadth_first_traversal()

# depth first in order print--------------------------------------------------------------------------------
print(" in order print trees")
T.inorder(n1)

# dfs preorder

print(" pre order print trees")
T.preorder(n1)

print("in breadth print trees ")

for i in range(0, len(List_of_nodes2)):
    node = List_of_nodes2[i]
    print(node.data)

found = T.search(8)
print("found the element in Tree %s" %found)