class BSTNode:
    def search_range(self, lower_bound, upper_bound):     
        result = []   

        if self.val.gamertag >= lower_bound and self.val.gamertag <= upper_bound:
            result.append(self.val)

        # Recursively traverse the left subtree
        if self.left:
            # if the current node's value is greater than the lower bound.
            if self.val.gamertag >= lower_bound:
                result.extend(self.left.search_range(lower_bound, upper_bound))
        # Recursively traverse the right subtree
        if self.right:
            # if the current node's value is less than the upper bound.
            if self.val.gamertag <= upper_bound:
                result.extend(self.right.search_range(lower_bound, upper_bound))

        return result                    

        
    def preorder(self, visited):        
        visited.append(self.val)        
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)    
        return visited   
    

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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
