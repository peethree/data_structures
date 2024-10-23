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
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        # While the new node isn't the root of the tree and its parent is red
        while new_node != self.root and new_node.parent.red == True:
            # If the parent is a right child
            if new_node.parent == new_node.parent.parent.right:
                # Set uncle to the parent's sibling
                uncle = new_node.parent.parent.left

                # If the uncle is red
                if uncle.red == True:
                    # Set the parent to black
                    uncle.red = False
                    # Set the parent to black
                    new_node.parent.red = False
                    # Set the grandparent to red
                    new_node.parent.parent.red = True
                    # Set the new node to be equal to the grandparent
                    # this will allow the loop to continue the recoloring process up the tree
                    new_node = new_node.parent.parent
                # if the uncle is black
                else:                    
                    # If the new node is a left child
                    if new_node == new_node.parent.left:
                        # Set the new node to its parent
                        new_node = new_node.parent
                        # Rotate the tree right around the new node                        
                        self.rotate_right(new_node)

                    # Set the parent to black
                    new_node.parent.red = False
                    # Set the grandparent to red
                    new_node.parent.parent.red = True
                    # Rotate the tree left around the grandparent
                    self.rotate_left(new_node.parent.parent)
                    
                    
            # Otherwise, if the parent is a left child:   
            else:
                # Set uncle to the parent's sibling
                uncle = new_node.parent.parent.right
                # If the uncle is red
                if uncle.red == True:
                    # Change the uncle to black
                    uncle.red = False
                    # Set the parent to black
                    new_node.parent.red = False
                    # Set the grandparent to red
                    new_node.parent.parent.red = True
                    # Set the new node to its grandparent
                    new_node = new_node.parent.parent
                # if uncle is black
                else:
                    # If the new node is a right child
                    if new_node == new_node.parent.right:  
                        # Set the new node to its parent
                        new_node = new_node.parent
                        # Rotate the tree left around the new node
                        self.rotate_left(new_node)                        
                    # Set the parent to black
                    new_node.parent.red = False
                    # Set the grandparent to red
                    new_node.parent.parent.red = True
                    # Rotate the tree right around the grandparent
                    self.rotate_right(new_node.parent.parent)                    
        # Set the root to black
        self.root.red = False
                    
                
                

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, x):
        if x == self.nil or x.right == self.nil:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        if x == self.nil or x.left == self.nil:
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
