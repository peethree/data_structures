class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()

        for i in range(len(document)):
            level = self.root
            
            for j in range(i, len(document)):
                char = document[j]               

                # check if the character is in the variations dict, replace it with the real value if so
                if char in variations:                    
                    char = variations[char]              
                
                if char not in level:
                    break
                    
                level = level[char]
                
                if self.end_symbol in level:
                    matches.add(document[i:j+1])
        return matches
  

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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
