class Trie:
    def find_matches(self, document):

        # Create a new set() to store the matches
        matches = set()

        # Loop over all the indexes of the characters in the document
        for i in range(len(document)):
            # Create a temporary level variable to hold the current level (a dictionary), 
            # and initialize it to the root of the trie.
            level = self.root
            # Use a nested loop to iterate over all the indexes of characters in the document, 
            # but start at the current index of the outer loop.
            for j in range(i, len(document)):
                char = document[j]
                if char not in level:
                    break
                else:
                    level = level[char]

                if self.end_symbol in level:
                    matches.add(document[i:j+1])

        return matches 

    """
    Suppose we have:

    document = "cat"
    self.root = {"c": {"a": {"t": {"*": True}}}, "a": {"t": {"*": True}}}
    This trie contains the words "cat" and "at".

    Here's how the loops would progress:

    Outer loop (i = 0):

    i = 0, level = self.root
    Inner loop starts:
    j = 0, char = 'c'
    j = 1, char = 'a'
    j = 2, char = 't'
    Outer loop (i = 1):

    i = 1, level = self.root
    Inner loop starts:
    j = 1, char = 'a'
    j = 2, char = 't'
    Outer loop (i = 2):

    i = 2, level = self.root
    Inner loop starts:
    j = 2, char = 't'

    In each iteration of the inner loop, 
    you would check if char exists in the current level of the trie, 
    and if so, move to the next level.
    """        

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
