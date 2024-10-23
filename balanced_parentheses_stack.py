def is_balanced(input_str):    

    # parentheses have to start with ( and close with ) 

    # closed_count = 0
    # open_count = 0    

    # if len(input_str) > 0:

    #     if input_str[0] != "(":            
    #         return False
    #     if input_str[-1] != ")":
    #         return False

    # for char in input_str:
    #     if char == "(":
    #         open_count += 1
    #     elif char == ")":
    #         closed_count += 1
    # if open_count == closed_count:
    #     return True
    # return False

     
    stack = Stack() 
    
    for char in input_str:
        if char == "(":
            # Push open parentheses onto the stack
            stack.push(char)          
        elif char == ")":
            # If the stack is empty when trying to pop, parentheses are unbalanced
            if stack.pop() is None:                
                return False  
    # Check if the stack is empty (all open parentheses have matching close parentheses)
    return stack.peek() is None          
                               

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
