class BSTNode:
    def preorder(self, visited):

        # Visit the value of the current node by appending its value to the visited array
        visited.append(self.val)

        # Recursively traverse the left subtree
        if self.left:
            self.left.preorder(visited)

        # Recursively traverse the right subtree
        if self.right:
            self.right.preorder(visited)

        # Return the array of visited nodes
        return visited
    
    
    def postorder(self, visited):
        # returns a list of the values in the order they are visited,         
        # and it takes as an argument the ordering of values 
        # we have visited so far

        # Recursively traverse the left subtree
        if self.left:
            self.left.postorder(visited)          

        # Recursively traverse the right subtree
        if self.right:
            self.right.postorder(visited)

        # Visit the value of the current node by 
        # appending its value to the visited array
        visited.append(self.val)

        return visited
    
    def inorder(self, visited):
        
        # Recursively traverse the left subtree
        if self.left:
            self.left.inorder(visited)

        # Visit the value of the current node by pushing its value onto the visited array
        visited.append(self.val)

        # Recursively traverse the right subtree
        if self.right:
            self.right.inorder(visited)

        # Return the list of nodes visited so far
        return visited


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
