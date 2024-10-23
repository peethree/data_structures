class LLQueue:
    def remove_from_head(self):
        # It should remove the first item from the queue and return it. 
        # If the queue is empty, just return None.
        if self.head is None:
            return None
    
        temp = self.head
        # if the first node in the list has a node after it
        if self.head.next is not None:
            # point self.head to the node next to it
            self.head = self.head.next
        # if it's the node in the list, set both head and tail to None
        else:
            self.head = None
            self.tail = None
        return temp             
  

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
