class BSTNode:  
    
    def height(self):
        if self.val is None:
            return 0  

        height_left = 0
        height_right = 0
            
        if self.left:                      
            height_left += self.left.height()

        if self.right:                     
            height_right += self.right.height()

        return max(height_left, height_right) + 1          


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
