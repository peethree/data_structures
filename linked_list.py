class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        # iterate over all the nodes in the list
        # starting with the head
        node = self.head

        # when node is none, end of linked list has been reached
        while node is not None: 
            #The yield statement is used to return the current node to the caller. 
            # It pauses the function and allows the iteration to continue from this point on the next call.
            yield node
            node = node.next
             

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
    

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:               
            # Instead of iterating to find the last node, 
            # add_to_tail should set the tail's next to the given node, 
            # then make that node the new tail.
            self.tail.set_next(node)
            self.tail = node

    def add_to_head(self, node):
        # if no head, set tail to current node
        if self.head is None:
            self.tail = node
        
        # set the node's next to the previous head
        node.set_next(self.head)
        # set the list's new head to the given node
        self.head = node  
        


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
    
# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.next = node3

# Create linked list and set head
linked_list = LinkedList()
linked_list.head = node1


for node in linked_list:
    print(node.val)

"""
In Python, you can insert elements into a list using the standard methods:

.insert()
.append()
For removing elements from a list, you can use:

.remove()
.pop()
.insert() and .remove() operate on elements at a specific position in a list, while .append() and .pop() insert or remove elements at the end of a list.

To .append() or .pop() an item at the end of a list requires one step. It's constant time, O(1).

To .insert() or .remove() an item at any index besides the end, requires shifting all other items at greater indexes to make room or fill the void. It's time complexity is the size of the list, O(n).

The structure of lists means each item has a fixed position, its index. Contrast that with linked lists, where the position of each item is not fixed. Each item knows the next item in the list by a pointer. So item positions don't need to change, only change the pointers. You can insert and remove items anywhere in the list without moving the entire list. If you have a pointer to the tail, and to the head, adding and removing can be done in constant time, O(1) by adjusting those pointers as needed.

For this reason, linked lists have a performance advantage over normal lists when implementing a queue (FIFO), in which elements are continuously inserted at the end and removed at the beginning of the list. But they perform similarly to a list when implementing a stack (LIFO), in which elements are inserted and removed at the end of the list.

"""