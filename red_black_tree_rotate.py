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

    def rotate_left(self, x):
        # If x is nil or x's right child is nil, return. Nothing to do here.
        if x == self.nil or x.right == self.nil:
            return

        # Let y be x's right child.
        y = x.right
        # Set x's right child to be y's left child.
        x.right = y.left

        # If y's left child isn't a nil leaf node, 
        # set y's left-child's parent to x
        if y.left != self.nil:
            y.left.parent = x
            
        # Set y's parent to x's parent
        y.parent = x.parent   

        # If x is the root, set the root to y
        if x == self.root:
            self.root = y
        else:
            # Otherwise, if x is its parent's left child, set x's parent's left child to y
            if x == x.parent.left:
                x.parent.left = y
            # Otherwise, if x is its parent's right child, set x's parent's right child to y
            if x == x.parent.right:
                x.parent.right = y

        # Set y's left child to be x
        y.left = x
        # Set x's parent to be y
        x.parent = y
   

    def rotate_right(self, x):
        # inverted rotate_left
        if x == self.nil or x.left == self.nil:
            return

        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent  

        if x == self.root:
            self.root = y
        else:
            if x == x.parent.right:
                x.parent.right = y
            if x == x.parent.left:
                x.parent.left = y

        y.right = x
        x.parent = y          
    

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
