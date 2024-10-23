class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # If the node doesn't have a value yet, just use the given value and be done
        if self.val is None:
            self.val = val    
            return        

        # If the node's value is equal to the given value, just be done, no duplicates allowed
        if self.val == val:
            return       

        # If the given value is less than the node's value and the node doesn't have a left child, 
        # create a new left child node with the given value
        if val < self.val and self.left is None:
            self.left = BSTNode(val)
            return

        # If the given value is less than the node's value and the node does have a left child, 
        # recursively call insert on that left child
        if val < self.val and self.left is not None:
            self.left.insert(val)
            return

        if val > self.val and self.right is None:
            self.right = BSTNode(val)
            return

        if val > self.val and self.right is not None:
            self.right.insert(val)
           

        
