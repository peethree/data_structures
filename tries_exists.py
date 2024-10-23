class Trie:
    def exists(self, word):

        # Loop over each nested dictionary in the trie associated with the letters in the word.
        current = self.root

        # loop over every character
        for char in word:
            # if the current character is in current dict
            if char in current:
                # update current to be the next character's dict
                current = current[char] 
            # if the current character is not in the dict, no point looking further
            else:
                return False

        """
        Once the loop has ended, 
        that's the point at which you check whether self.end_symbol is in current. 
        This will indicate whether the word was successfully found 
        and terminated in the trie.
        """        
        if self.end_symbol in current:
            return True                               
        return False        
  

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
