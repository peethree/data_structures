class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil


    def insert(self, val):
        """Create the new node"""
        # Create a new RBNode from the given input value        
        node = RBNode(val)

        # The new node shouldn't have a parent yet

        # The new node's left and right children should be nil
        node.left = self.nil
        node.right = self.nil
        
        # The new node is red. 
        node.red = True

        """Find the parent of the new_node if there will be one"""
        # Initialize a parent variable to None
        parent = None
        # Initialize a current variable to the root node of the tree
        current = self.root

        # While current isn't a nil node
        while current != self.nil:
            # Set parent to the current
            parent = current
            # If the new_node's value is less than the current node's, 
            # set current to its own left child. If it's greater, set to its right child. 
            # If the values are equal, just return because this value is a duplicate.
            if node.val < current.val:
                current = current.left
            elif node.val > current.val:
                current = current.right
            else:
                return
            

        """Insert the new node"""
        # Set the new node's parent to the parent we just found
        node.parent = parent
        # If the parent is None, we are dealing with a new root, 
        # so set the tree's root data member to the new node
        if parent is None:
            self.root = node
        # Otherwise, compare the values of the parent and new node and set 
        # the parent's left or right child based on the results
        
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

       
        
