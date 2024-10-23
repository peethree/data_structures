class Trie:
    def add(self, word):
        # Assign a temporary variable current to the root dictionary of the trie.
        current = self.root

        # Loop over each character in the word
        for char in word:
            # If the character is not a key in the current dictionary, 
            # add it and assign a new empty dictionary to it.
            if char not in current:
                current[char] = {}
            # Update the current dictionary to point to the child dictionary 
            # corresponding to the character in the loop.
            current = current[char]            
            """
            Once you've ensured all the dictionaries exist, 
            add the self.end_symbol to the dictionary of the last character in the word. 
            This will indicate that this is a complete word and not just a prefix of another word.
            """
            if char == word[-1]:
                current[self.end_symbol] = True                              
 

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
