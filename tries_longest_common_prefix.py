class Trie:
    def longest_common_prefix(self):
        # Initialize a variable current that references the root of the trie
        current = self.root
        # Initialize a variable prefix to an empty string
        prefix = ""

        # Enter a forever while loop
        while True:            

            # check for end symbol at start of the loop in case the current dictionary object is boolean
            if self.end_symbol in current:
                return prefix
                
            # Get the "children" in the current dictionary (the number of valid keys in the dictionary)    
            children = current.keys()
        

            # If a child is an end_symbol, break the loop.
            if self.end_symbol == children:
                break
            
            # If there is only one child, append the character to the prefix string and 
            # update the current dictionary to point to the child dictionary corresponding to the character.   
            if len(children) == 1:                
                prefix += list(children)[0]                    
                current = current[list(children)[0]]

            # If there are multiple children or no children, break the loop.
            if len(children) == 0 or len(children) > 1:
                break                                  

        return prefix                             
        
    

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
