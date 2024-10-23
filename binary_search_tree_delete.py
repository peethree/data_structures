class BSTNode:
    def delete(self, val):

        # if current value is none: empty tree or leaf node (deletion already occurred) return none
        if self.val is None:
            return None

        if val < self.val:
            # if there is a left child, recursively call delete method on the left child 
            # with value to delete and set the left child to the return val of the recursive call
            if self.left is not None:
                self.left = self.left.delete(val)
            # Regardless of whether the left child exists or not, 
            # return the current node.
            return self

        # mirrored for the right child
        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self


        # If there is no right child, return the left child. 
        # This effectively deletes the current node by bypassing it.
        if self.right is None:
            return self.left
        # mirrored for left child
        if self.left is None:
            return self.right        
        
        # This is the node with the smallest value 
        # that is still larger than self.val
        # by traversing down the left side of the right subtree
       
        min_larger_node = self.right

        while min_larger_node.left:
            # This is the node with the smallest value that is still larger than self.val
            min_larger_node = min_larger_node.left

        # Replace self.val with min_larger_node.val.
        self.val = min_larger_node.val
        # Delete min_larger_node.val from the right subtree 
        # and set the right child to the return value of the recursive call.
        self.right = self.right.delete(min_larger_node.val)       
      
        return self                            
   

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
