class BSTNode:
    def exists(self, val):
        # It should take a value as input and return True if the value exists in the tree, 
        # and False if it doesn't.
        
        if val == self.val:
            return True
            
        # if self.left is not none, recursively traverse left tree
        if self.left and val < self.val:
            return self.left.exists(val)    

        # Only checks the left subtree if the value is less than the current node's value, 
        # and only checks the right subtree if the value is greater.
        if self.right and val > self.val:
            return self.right.exists(val)

        return False            
        

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
